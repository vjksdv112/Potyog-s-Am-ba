import numpy as np
import os
import time
from rich import print
from rich.console import Console
from agent import random_agent

"""
AI Használat összegző
AI modell: Google Gemini 3.1 Pro
Dátum: 2026. április 26.
Cél: A numpy, rich, stb mélyebb megértése, feladat logikájának a megértése implementálása, példa feladatok generálása és megoldasa
Prompt1: "A main.py-ban a is_valid_move és a drop_piece függvényekben beégetett 6-os sorindexeket használok. Hogyan tudom a board.shape attribútumot felhasználni arra, hogy a kód automatikusan felismerje a tábla méretét, és dinamikusan mindig a legfelső sort vizsgálja, függetlenül attól, hogy 6x7-es vagy 20x20-as táblát inicializáltam?"
Prompt2: "A check_win függvényemben az iterációs határok fixen 6 - 3 és 7 - 3 formában szerepelnek a 4-es nyerőhosszhoz. Ha bevezetek egy win_length paramétert, mi a matematikai szabálya a for ciklusok biztonságos határának (hogy ne kapjak IndexError-t), ha a tábla mérete rows és cols?"
Prompt3: "Szeretnék egy 'VISSZA' funkciót rakni a kódba. Amikor elmentem az aktuális táblát a saved_board változóba, miért rossz a saved_board = board értékadás megoldás?"
Prompt4: "Milyen ellenőrzést kell írnom az inicializálásnál, hogy a játék ne engedjen olyan felállást létrehozni, ahol a win_length nagyobb, mint magának a táblának a méretei?"
Használat módja: Részleges kódgenerálás, mélyebb megértése a Libraries-eknek, optimalizálás
"""



console = Console()

def generate_column_labels(cols):
    """Oszlopcímkék generálása dinamikusan."""
    return [chr(ord("A") + i) for i in range(cols)]

def create_board(rows, cols):
    """Létrehoz egy felhasználó által meghatározott méretű játéktáblát"""
    return np.zeros((rows, cols), dtype=int)

def print_board(board, column_labels, clear_screen=True):
    """Kiírja az aktuális játéktáblát színkódolt korongokkal."""
    if clear_screen:
        os.system('cls' if os.name == 'nt' else 'clear')
    for row in reversed(board):
        print(" ".join("[red]O[/red]" if cell == 1 else "[green]O[/green]" if cell == 2 else "." for cell in row))
    print(" ".join(column_labels))

def is_valid_move(board, col):
    """Ellenőrzi, hogy egy lépés érvényes-e."""
    return board[board.shape[0] - 1, col] == 0

def drop_piece(board, col, piece):
    """Ejt egy korongot a megadott oszlopba."""
    for row in range(board.shape[0]):
        if board[row, col] == 0:
            board[row, col] = piece
            return

def check_win(board, piece, win_length):
    """Ellenőrzi, hogy a megadott játékos nyert-e az új dinamikus szabállyal."""
    rows, cols = board.shape
    for row in range(rows):
        for col in range(cols - win_length + 1):
            if all(board[row, col + i] == piece for i in range(win_length)): return True
    for row in range(rows - win_length + 1):
        for col in range(cols):
            if all(board[row + i, col] == piece for i in range(win_length)): return True
    for row in range(rows - win_length + 1):
        for col in range(cols - win_length + 1):
            if all(board[row + i, col + i] == piece for i in range(win_length)): return True
    for row in range(win_length - 1, rows):
        for col in range(cols - win_length + 1):
            if all(board[row - i, col + i] == piece for i in range(win_length)): return True
    return False

def is_draw(board):
    """Ellenőrzi, hogy döntetlen-e a játék."""
    return np.all(board != 0)

def play_game():
    """A fő játékhurok, amely lehetővé teszi a Connect 4 játékot és a visszavonást."""
    while True:
        parts = console.input("Add meg a sorok, oszlopok és a nyerő hosszt (pl. 6 7 4): ").split()
        if len(parts) == 3 and all(p.isdigit() for p in parts) and all(int(p) > 0 for p in parts):
            rows, cols, win_length = map(int, parts)
            if not (rows < win_length and cols < win_length):
                break
        console.print("[bold red]Érvénytelen bemenet. Próbáld újra![/bold red]")

    column_labels = generate_column_labels(cols)
    board = create_board(rows, cols)
    game_over = False
    turn = 0

    # --- Visszavonáshoz a változók ---
    saved_board = None
    can_undo = False

    print_board(board, column_labels)

    while not game_over:
        if turn == 0:
            prompt_text = f"[red]Játékos 1[/red], válassz egy oszlopot ({column_labels[0]}-{column_labels[-1]}) vagy írd be: VISSZA: " if can_undo else f"[red]Játékos 1[/red], válassz egy oszlopot ({column_labels[0]}-{column_labels[-1]}): "
            col_input = console.input(prompt_text).upper()

            # Visszavonás (Undo) logika feldolgozása
            if col_input == "VISSZA":
                if can_undo:
                    board = np.copy(saved_board)
                    can_undo = False
                    print_board(board, column_labels)
                    continue
                else:
                    console.print("[bold red]Jelenleg nem lehet mit visszavonni![/bold red]")
                    continue

            if col_input in column_labels:
                saved_board = np.copy(board)
                can_undo = True
                col = column_labels.index(col_input)
            else:
                console.print(f"[bold red]Érvénytelen bemenet.[/bold red] Válassz egy oszlopot {column_labels[0]} és {column_labels[-1]} között.")
                continue
        else:
            time.sleep(1)
            col = random_agent(board, is_valid_move)
            print(f"[green]Játékos 2 (AI)[/green] az {column_labels[col]} oszlopot választotta")

        if is_valid_move(board, col):
            drop_piece(board, col, turn + 1)
            print_board(board, column_labels, clear_screen=turn == 0)

            if check_win(board, turn + 1, win_length):
                print(f"[bold red]Játékos {turn + 1} nyert![/bold red]" if turn == 0 else f"[bold green]Játékos {turn + 1} nyert![/bold green]")
                if can_undo:
                    vissza = console.input("[bold yellow]A játék véget ért. Szeretnéd visszavonni az utolsó kört? (I/N): [/bold yellow]").upper()
                    if vissza == 'I':
                        board = np.copy(saved_board)
                        can_undo = False
                        turn = 0
                        print_board(board, column_labels)
                        continue
                game_over = True

            elif is_draw(board):
                print("[bold yellow]Döntetlen![/bold yellow]")
                if can_undo:
                    vissza = console.input("[bold yellow]A játék véget ért. Szeretnéd visszavonni az utolsó kört? (I/N): [/bold yellow]").upper()
                    if vissza == 'I':
                        board = np.copy(saved_board)
                        can_undo = False
                        turn = 0
                        print_board(board, column_labels)
                        continue
                game_over = True
            else:
                turn = 1 - turn
        else:
            console.print("[bold red]Az oszlop megtelt.[/bold red]")

if __name__ == "__main__":
    play_game()