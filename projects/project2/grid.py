from typing import List
from random import choice
from datastructures.array2d import Array2D
from projects.project2.cell import Cell

class Grid:
    def __init__(self, width:int, height: int) -> None:
        cells: List[List[Cell]]= []

        for row in range(width):
            cells.append([])
            for col in range(height):
                is_alive = random.choice([True, False])
                cells[row].append(Cell(is_alive=is_alive))

        self.grid: Array2D = Array2D(starting_sequence = [[]], data_type=Cell)

    def display(self):
        print(self.grid)