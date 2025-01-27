"""Midterm 2 Q3.
A little bit Waldo-ish, a little bit Sudoku-ish.
We want to determine whether a grid contains at least
one column in which the tiles include all the colors
of a given spectrum.
"""
from typing import List, Set
import enum

class Color(enum.Enum):
    """Colors in the rainbow"""
    red = "r"
    orange = "o"
    yellow = "y"
    green = "g"
    blue = "b"
    indigo = "i"
    violet = "v"
    black = "k"
    white = "w"

    def __str__(self) -> str:
        return self.name

# Spectra are lists of distinct colors, ranging from the
# the whole rainbow to much smaller collections.
# For example ...
RAINBOW = [Color.red, Color.orange, Color.yellow,
           Color.green, Color.blue, Color.indigo,
           Color.violet ]

PRIMARIES = [ Color.red, Color.green, Color.blue ]

BW = [Color.black, Color.white]


class Grid:
    """A grid of colors.
    It wraps a list of lists of Color objects,
    which we assume to be rectangular
    (same number of columns in each row)
    """
    def __init__(self, gridspec: List[List[Color]]):
        """gridspec is a matrix, i.e., each row same length"""
        self._tiles = gridspec

    def __str__(self) -> str:
        """Line up color letters neatly in columns"""
        rows = []
        for row in self._tiles:
            names = [tile.value for tile in row]
            rows.append(" ".join(names))
        return "\n".join(rows)

    def some_column_all_colors(self, spectrum: List[Color]) -> bool:
        """True if at least one column has all the colors
        of the spectrum.
        (This was the midterm question)
        """
        columns = self.columns()
        for column in columns:
            if all(color in column for color in spectrum):
                return True
        return False
        # Hints:  A set would be a useful data structure.
        # Recall the set methods
        #    s = set([x, y, z])  to create set from a list
        #    s.len()  to count elements in a list
        #    s.discard(y) to remove an element

    def columns(self) -> List[List[Color]]:
        result = [[]]
        if len(self._tiles) == 0:
            return result
        for i in range(len(self._tiles[0])):
            column = []
            for x in self._tiles:
                column.append(x[i])
            result.append(column)
        return result


    # The following methods were added for live coding

    def all_columns_all_colors(self, spectrum: List[Color]) -> bool:
        """True if each column has all the colors of the spectrum"""
        return False

    def some_column_distinct_colors(self, spectrum: List[Color]) -> bool:
        """True if all the colors in at least one column are distinct"""
        return False

    def all_rows_distinct_colors(self, spectrum: List[Color]) -> bool:
        """True if for all rows, all tiles have different colors"""
        return False


def main():
    """Simple example ... see test_q3.py for more"""
    grid = Grid(
        [[Color.red, Color.green, Color.blue]
        ,[Color.green, Color.blue, Color.red]
        ,[Color.green, Color.red, Color.blue]])
    ###                ^ All primary colors in 2nd column
    print(grid)
    assert grid.some_column_all_colors(PRIMARIES)
    assert not grid.some_column_all_colors(RAINBOW)

if __name__ == "__main__":
    main()