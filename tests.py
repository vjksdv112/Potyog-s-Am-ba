import unittest
import numpy as np
from main import create_board, drop_piece, check_win


class TestAmoeba(unittest.TestCase):


    def test_tabla_meret(self):
        tabla = create_board(10, 15)
        self.assertEqual(tabla.shape, (10, 15))
        self.assertTrue(np.all(tabla == 0))

    def test_nyeres_vizszintesen(self):
        tabla = create_board(8, 8)

        for i in range(5):
            drop_piece(tabla, i, 1)

        self.assertTrue(check_win(tabla, 1, 5))

        self.assertFalse(check_win(tabla, 1, 6))

    def test_nyeres_fuggolegesen(self):
        tabla = create_board(6, 7)

        drop_piece(tabla, 2, 2)
        drop_piece(tabla, 2, 2)
        drop_piece(tabla, 2, 2)

        self.assertTrue(check_win(tabla, 2, 3))


    def test_visszavonas_alap(self):
        tabla = create_board(6, 7)
        mentett_tabla = np.copy(tabla)

        drop_piece(tabla, 0, 1)

        tabla = np.copy(mentett_tabla)
        self.assertTrue(np.all(tabla == 0))

    def test_visszavonas_tobb_lepesnel(self):

        tabla = create_board(6, 7)

        drop_piece(tabla, 0, 1)
        mentett = np.copy(tabla)

        drop_piece(tabla, 1, 2)

        tabla = np.copy(mentett)

        self.assertEqual(tabla[0, 0], 1)
        self.assertEqual(tabla[0, 1], 0)

    def test_memoria_masolas_hibatlan(self):
        tabla = create_board(6, 7)
        mentett = np.copy(tabla)

        drop_piece(tabla, 3, 1)

        self.assertTrue(np.all(mentett == 0))


if __name__ == "__main__":
    unittest.main()