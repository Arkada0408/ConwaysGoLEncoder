import copy
from typing import List


def generate_board(width: int, height: int):
    board: List[List[int]] = []
    for row in range(0, height):
        board.append([])
        for column in range(0, width):
            board[row].append(0)
    return board


def previous_row_id(row_id, board: List[List[int]]) -> int:
    if row_id == 0:
        return -1
    return row_id-1


def next_row_id(row_id, board: List[List[int]]) -> int:
    if row_id == len(board)-1:
        return 0
    return row_id+1


def previous_column_id(column_id, board: List[List[int]]) -> int:
    if column_id == 0:
        return -1
    return column_id-1


def next_column_id(column_id, board: List[List[int]]) -> int:
    if column_id == len(board[0])-1:
        return 0
    return column_id+1


def iterate_board(board: List[List[int]]):
    new_board = copy.deepcopy(board)
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            neighbors = [board[previous_row_id(row, board)][previous_column_id(column, board)],
                         board[previous_row_id(row, board)][column],
                         board[previous_row_id(row, board)][next_column_id(column, board)],
                         board[row][previous_column_id(column, board)],
                         board[row][next_column_id(column, board)],
                         board[next_row_id(row, board)][previous_column_id(column, board)],
                         board[next_row_id(row, board)][column],
                         board[next_row_id(row, board)][next_column_id(column, board)]]
            neighbor_amount = sum(neighbors)
            if board[row][column] == 0:
                if neighbor_amount == 3:
                    new_board[row][column] = 1
            elif neighbor_amount < 2 or neighbor_amount > 3:
                new_board[row][column] = 0
            else:
                new_board[row][column] = 1
    return new_board


def draw_board(board: List[List[int]]):
    for row in range(0, len(board)):
        print()
        for column in range(0, len(board[row])):
            if board[row][column] == 1:
                ch = "■"
            else:
                ch = "□"
            print(f"{ch} ", end="")
    print()

