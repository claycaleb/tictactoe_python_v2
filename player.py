import numpy as np


class Player:
    def __init__(self, char, cell, cells, goes_first):
        self.char = char
        self.cell = cell
        self.cells = cells
        self.goes_first = goes_first

    def is_winner(self) -> bool:
        grid_matrix = np.array([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]])

        for i in range(3):
            for array in [grid_matrix[i], grid_matrix[:, i]]:
                win = all(cell in self.cells for cell in array)
                if win:
                    return win

        for array in [grid_matrix.diagonal(), np.fliplr(grid_matrix).diagonal()]:
            win = all(cell in self.cells for cell in array)
            if win:
                return win
