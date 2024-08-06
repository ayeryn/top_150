# 52

from typing import Dict


def n_queens(n: int) -> list[list[str]]:
    ans = []

    def build_solution(board: Dict[int, int]) -> list[str]:
        """
        Build a solution array based on the board hashmap.

        Args:
        board (dict): A hashmap representing the board configuration.

        Returns:
        list: A list of strings representing the solution array.
        """
        ret = ["" for _ in range(n)]
        for row in board:
            ret[row] = "." * board[row] + "Q" + "." * (n - 1 - board[row])
        return ret

    def available_cols(x: int, board: Dict[int, int]):
        """
        Returns a set of possible sol positions for the queen given its current row and the board state.

        Args:
            x (int): The current row position of the queen.
            board (list): A list representing the current state of the board with queens placed.

        Returns:
            set: A set of possible col positions for the queen on row x.
        """

        # Define search space - all cols
        # Use a set for O(1) membership and removal
        ret = set([i for i in range(n)])
        if len(board) == 0:
            # No Queen has been placed yet, all cols available
            return ret

        for row in board:
            # Naturally excluding all indexes on existing rows because hashmap

            # remove same col
            ret.discard(board[row])

            # remove same diagonal
            tb_diag_col = x + board[row] - row  # left-top to right-bottom
            bt_diag_col = board[row] + row - x  # left-bottom to right-top
            ret.discard(tb_diag_col)
            ret.discard(bt_diag_col)
        return ret

    def solve(x: int, state: Dict[int, int]) -> None:
        """
        Recursive function to solve the board by exploring possible solutions by row.

        Args:
            x (int): The current row being considered.
            board (Dict[int, int]): A dictionary representing the current state of the board.

        Returns:
            None
        """
        nonlocal ans

        if len(state) == n:
            # Found valid solution
            ans.append(build_solution(state))
            return

        solutions = available_cols(x, state)
        if len(solutions) == 0:
            return

        for i in solutions:
            state[x] = i  # Update state
            solve(x + 1, state)  # Solve for next row
            del state[x]  # Backtrack

    solve(0, {})
    return ans
