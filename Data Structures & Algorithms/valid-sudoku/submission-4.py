class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        row = 0
        hasSeen = [False] * 10
        while row < 9:
            for i in board[row]:
                if i == ".":
                    continue
                if hasSeen[int(i)]:
                    return False
                hasSeen[int(i)] = True
            row += 1
            hasSeen = [False] * 10

        # check col
        row = 0
        col = 0
        while col < 9:
            while row < 9:
                if board[row][col] == ".":
                    row += 1
                    continue
                if hasSeen[int(board[row][col])]:
                    return False
                hasSeen[int(board[row][col])] = True
                row += 1
            col += 1
            row = 0
            hasSeen = [False] * 10

            
        # check square
        gridRow = 0
        gridCol = 0
        row = 0
        col = 0
        while gridRow < 3:
            while gridCol < 3:
                while row < 3:
                    while col < 3:
                        rowIndex = row + (gridRow * 3)
                        colIndex = col + (gridCol * 3)
                        if board[rowIndex][colIndex] == ".":
                            col += 1
                            continue
                        if hasSeen[int(board[rowIndex][colIndex])]:
                            return False
                        hasSeen[int(board[rowIndex][colIndex])] = True
                        col += 1
                    col = 0
                    row += 1
                row = 0
                gridCol += 1
                hasSeen = [False] * 10
            gridRow += 1

        return True