from typing import List
import random
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
from copy import copy

class Grid:
    def __init__(self, width:int, height: int) -> None:
        cells: List[List[Cell]]= []

        for row in range(height):
            cells.append([])
            for col in range(width):
                is_alive = random.choice([True, False])
                cells[row].append(Cell(is_alive=is_alive))

        self.grid: Array2D = Array2D(starting_sequence = cells, data_type=Cell)

    def display(self):
        for row in range(self.grid.row_len):
            for col in range(self.grid.column_len):
                cell = self.grid[row][col]
                print("🦠" if cell.is_alive else "⬛️", end="")
            print()

    def num_neighbors(self, row:int, col:int) -> int:
        count = 0

        for r in range (row-1, row+2):
            for c in range(col-1,col+2):
                if r==row and c==col:
                    # skips the center cell
                    continue

                if r>=0 and r < self.grid.row_len and c>=0 and c < self.grid.column_len:
                    if self.grid[r][c].is_alive:
                        count+=1
        return count

    def next_generation(self):
        new_gen = Array2D.empty(self.grid.row_len, self.grid.column_len, Cell)

        for row in range(self.grid.row_len):
            for col in range(self.grid.column_len):
                alive_neighbors = self.num_neighbors(row, col)
                cell = self.grid[row][col]

                if alive_neighbors == 3 or (alive_neighbors == 2 and cell.is_alive):
                    new_gen[row][col] = Cell(is_alive=True)
                else:
                    new_gen[row][col] = Cell(is_alive=False)

        self.grid = new_gen

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        if self.grid.row_len != other.grid.row_len or self.grid.column_len != other.grid.column_len:
            return False
        for row in range(self.grid.row_len):
            for col in range(self.grid.column_len):
                if self.grid[row][col].is_alive != other.grid[row][col].is_alive:
                    return False
        return True

            


