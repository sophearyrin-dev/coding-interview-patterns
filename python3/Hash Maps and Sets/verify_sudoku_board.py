from typing import List


def verify_sudoku_board(board: List[List[int]]) -> bool:
    # Create hash sets for each row, column, and subgrid to keep 
    # track of numbers previously seen on any given row, column, or 
    # subgrid.
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                continue
            # Check if 'num' has been seen in the current row, 
            # column, or subgrid.
            if num in row_sets[r]:
                return False
            if num in column_sets[c]:
                return False
            if num in subgrid_sets[r // 3][c // 3]:
                return False
            # If we passed the above checks, mark this value as seen 
            # by adding it to its corresponding hash sets.
            row_sets[r].add(num)
            column_sets[c].add(num)
            subgrid_sets[r // 3][c // 3].add(num)
    return True


//java


class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            HashSet<Character> setRow = new HashSet<>();
            HashSet<Character> setCol = new HashSet<>();
            HashSet<Character> setBox = new HashSet<>();

            for (int j = 0; j < 9; j++) {
                // Check row
                if (board[i][j] != '.' && !setRow.add(board[i][j])) {
                    return false;
                }

                // Check column
                if (board[j][i] != '.' && !setCol.add(board[j][i])) {
                    return false;
                }

                // Check 3x3 subgrid
                int rowIndex = i/3*3 + j/3;
                int colIndex = i%3*3 + j%3;
                if (board[rowIndex][colIndex] != '.' && !setBox.add(board[rowIndex][colIndex])) {
                    return false;
                }
            }
        }

        return true;
    }
}

