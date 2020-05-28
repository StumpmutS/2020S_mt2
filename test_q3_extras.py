import unittest
from q3_logic import *


# Weird spectrum just for testing
BWG = [Color.black, Color.white, Color.green]

class Test_1_Monochrome(unittest.TestCase):

    def test_1_full_bw(self):
        grid = Grid([[Color.black, Color.white, Color.black],
                     [Color.black, Color.white, Color.white]])
        self.assertTrue(grid.some_column_all_colors(BW))
        self.assertFalse(grid.some_column_all_colors(BWG))

    def test_2_not_in_column(self):
        grid = Grid([[Color.black, Color.white, Color.black],
                     [Color.black, Color.white, Color.black]])
        self.assertFalse(grid.some_column_all_colors(BW))

    def test_3_long_columns(self):
        grid = Grid([[Color.black, Color.white, Color.white],
                     [Color.black, Color.white, Color.white],
                     [Color.black, Color.white, Color.white],
                     [Color.black, Color.white, Color.white],
                     [Color.black, Color.white, Color.white],
                     [Color.black, Color.black, Color.white],
                     ])
        self.assertTrue(grid.some_column_all_colors(BW))
        self.assertFalse(grid.some_column_all_colors(BWG))


class Test_2_Rainbow(unittest.TestCase):
    def test_1_rainbow(self):
        # A grid with full rainbow of colors in third column
        grid = Grid(
            [[Color.red, Color.green, Color.red, Color.red]
            ,[Color.green, Color.red, Color.green, Color.green]
            ,[Color.blue, Color.orange, Color.blue, Color.orange]
            ,[Color.orange, Color.blue, Color.orange, Color.blue]
            ,[Color.indigo, Color.violet, Color.indigo, Color.violet]
            ,[Color.indigo, Color.yellow, Color.violet, Color.violet]
            ,[Color.blue,  Color.green, Color.yellow, Color.yellow]
            ,[Color.red, Color.green, Color.red, Color.red]])
        self.assertTrue(grid.some_column_all_colors(RAINBOW))
        self.assertFalse(grid.some_column_all_colors(BW))

    def test_2_rainbow(self):
        # No single column has all the rainbow colors
        grid = Grid([[Color.red, Color.green, Color.red, Color.red]
            ,[Color.green, Color.red, Color.green, Color.green]
            ,[Color.blue, Color.orange, Color.blue, Color.orange]
            ,[Color.orange, Color.blue, Color.orange, Color.blue]
            ,[Color.indigo, Color.violet, Color.indigo, Color.violet]
            ,[Color.indigo, Color.violet, Color.yellow, Color.violet]
            ,[Color.blue,  Color.green, Color.red, Color.yellow]
            ,[Color.red, Color.green, Color.yellow, Color.red]])
        self.assertFalse(grid.some_column_all_colors(RAINBOW))
        # But several columns have at least the primary colors
        self.assertTrue(grid.some_column_all_colors(PRIMARIES))

# Extras
# * All columns all colors,
# * some column distinct colors, and
# * all rows distinct colors.

class Test_3_All_Columns_All_Colors(unittest.TestCase):
    """For new method all_columns_all_colors"""
    def test_0(self):
        """Middle column does not have black"""
        grid = Grid([[Color.black, Color.white, Color.black],
                     [Color.white, Color.white, Color.white]])
        self.assertFalse(grid.all_columns_all_colors(BW))

    def test_1(self):
        """Each column does have both black and white"""
        grid = Grid([[Color.black, Color.white, Color.black],
                     [Color.white, Color.black, Color.white]])
        self.assertTrue(grid.all_columns_all_colors(BW))
        self.assertFalse(grid.all_columns_all_colors(BWG))

    def test_2(self):
        """Rows don't, but columns do have all colors of BWG"""
        grid = Grid([[Color.black, Color.black, Color.black],
                     [Color.white, Color.white, Color.white],
                     [Color.green, Color.green, Color.green]])
        self.assertTrue(grid.all_columns_all_colors(BWG))

    def test_3(self):
        """Checking complete spectrum is not same as checking duplicates"""
        grid = Grid([[Color.black, Color.black, Color.black],
                     [Color.white, Color.white, Color.white],
                     [Color.green, Color.green, Color.green],
                     [Color.black, Color.white, Color.green]])
        self.assertTrue(grid.all_columns_all_colors(BWG))

class Test_4_Some_Column_Distinct(unittest.TestCase):
    """For new method some_column_distinct_colors"""
    def test_0(self):
        """First and third columns have distinct colors"""
        grid = Grid([[Color.black, Color.white, Color.black],
                     [Color.white, Color.white, Color.white]])
        self.assertTrue(grid.some_column_distinct_colors(BW))
        # Still distinct even if we haven't used all colors
        self.assertTrue(grid.some_column_distinct_colors(BWG))

    def test_1(self):
        """No column has distict colors """
        grid = Grid([[Color.black, Color.white, Color.black],
                     [Color.white, Color.black, Color.white],
                     [Color.black, Color.white, Color.black]])
        self.assertFalse(grid.some_column_distinct_colors(BW))
        # Having a bigger spectrum doesn't change distinctness
        self.assertFalse(grid.some_column_distinct_colors(BWG))

    def test_3(self):
        """Checking complete spectrum is not same as checking duplicates"""
        grid = Grid([[Color.black, Color.black, Color.black],
                     [Color.white, Color.white, Color.white],
                     [Color.green, Color.green, Color.green],
                     [Color.black, Color.white, Color.green]])
        self.assertFalse(grid.some_column_distinct_colors(BWG))

# * all rows distinct colors.
class Test_5_All_Rows_Distinct(unittest.TestCase):
    """For new method all_rows_distinct_colors"""
    def test_0(self):
        """Duplicates in both rows"""
        grid = Grid([[Color.black, Color.white, Color.black],
                     [Color.white, Color.black, Color.green]])
        self.assertFalse(grid.all_rows_distinct_colors(BWG))


    def test_1(self):
        """Columns have duplicates, rows don't"""
        grid = Grid([[Color.black, Color.white, Color.green],
                     [Color.black, Color.green, Color.white],
                     [Color.white, Color.green, Color.black]])
        self.assertTrue(grid.all_rows_distinct_colors(BWG))

    def test_2(self):
        """More rows than columns"""
        grid = Grid([[Color.black, Color.white],
                     [Color.white, Color.green],
                     [Color.white, Color.black],
                     [Color.green, Color.black]])
        self.assertTrue(grid.all_rows_distinct_colors(BWG))


if __name__ == "__main__":
    unittest.main()