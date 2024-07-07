class Board:
    """
    Represents a Sudoku board.

    Attributes:
        board (list): A 9x9 grid representing the Sudoku puzzle. 
                      Zeros represent empty cells.
    """

    def __init__(self, board):
        """
        Initializes the Sudoku board.

        Args:
            board (list): A 9x9 list of lists representing the Sudoku puzzle.
        """
        self.board = board

    def __str__(self):
        """
        Returns a string representation of the board.

        Returns:
            str: A string with the Sudoku board where empty cells are represented by '*'.
        """
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        """
        Finds the next empty cell in the board.

        Returns:
            tuple: A tuple (row, col) of the empty cell's position, or None if there are no empty cells.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        """
        Checks if a number is valid in the specified row.

        Args:
            row (int): The row index.
            num (int): The number to check.

        Returns:
            bool: True if the number is not in the row, False otherwise.
        """
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        Checks if a number is valid in the specified column.

        Args:
            col (int): The column index.
            num (int): The number to check.

        Returns:
            bool: True if the number is not in the column, False otherwise.
        """
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """
        Checks if a number is valid in the 3x3 square containing the specified cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            num (int): The number to check.

        Returns:
            bool: True if the number is not in the 3x3 square, False otherwise.
        """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        """
        Checks if a number is valid in the specified cell.

        Args:
            empty (tuple): A tuple (row, col) of the cell's position.
            num (int): The number to check.

        Returns:
            bool: True if the number is valid in the row, column, and 3x3 square, False otherwise.
        """
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        """
        Solves the Sudoku puzzle using backtracking.

        Returns:
            bool: True if the puzzle is solvable, False otherwise.
        """
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False

def solve_sudoku(board):
    """
    Solves a given Sudoku puzzle and prints the result.

    Args:
        board (list): A 9x9 list of lists representing the Sudoku puzzle.
    
    Returns:
        Board: The solved Sudoku board.
    """
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

# Example Sudoku puzzle
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)
