def find(i, j, board):
    if board[i][j] == '.':
        return False
    if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
        return True
    return False


def range_board(removes, board, result):
    remove_count = 0
    for remove in removes:
        if board[remove[0]][remove[1]] != '.':
            remove_count += 1
            board[remove[0]][remove[1]] = '.'
        if board[remove[0]][remove[1] + 1] != '.':
            remove_count += 1
            board[remove[0]][remove[1] + 1] = '.'
        if board[remove[0] + 1][remove[1]] != '.':
            remove_count += 1
            board[remove[0] + 1][remove[1]] = '.'
        if board[remove[0] + 1][remove[1] + 1] != '.':
            remove_count += 1
            board[remove[0] + 1][remove[1] + 1] = '.'

    while True:
        is_fixed = False
        for i in range(len(board[0])):
            for j in range(len(board) - 1, 0, -1):
                if board[j][i] == '.' and board[j - 1][i] != '.':
                    board[j][i] = board[j - 1][i]
                    board[j - 1][i] = '.'
                    is_fixed = True
        if not is_fixed:
            break
    return remove_count


def solution(m, n, input):
    result = 0
    board = []
    for i in range(m):
        board.append(list(input[i]))

    while True:
        removes = []
        for i in range(m - 1):
            for j in range(n - 1):
                if find(i, j, board):
                    removes.append((i, j))
        if not removes:
            break
        result += range_board(removes, board, result)

    return result


if __name__ == '__main__':
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
