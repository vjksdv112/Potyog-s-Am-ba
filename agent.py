import random

def random_agent(board, is_valid_move):
    """Véletlenszerűen választ egy érvényes oszlopot."""
    valid_columns = [col for col in range(board.shape[1]) if is_valid_move(board, col)]
    return random.choice(valid_columns) if valid_columns else None
