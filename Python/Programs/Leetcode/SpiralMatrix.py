class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    @staticmethod
    def spirally_traverse(matrix, r, c):
        top = 0
        bottom = r - 1
        left = 0
        right = c - 1
        dir = 0
        result = []

        while top <= bottom and left <= right:
            # Traverse from left to right
            if dir == 0:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1

            # Traverse from top to bottom
            elif dir == 1:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1

            # Traverse from right to left
            elif dir == 2:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Traverse from bottom to top
            elif dir == 3:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

            # Update direction
            dir = (dir + 1) % 4

        return result


if __name__ == "__main__":
    # custom input
    # t = int(input())
    # for _ in range(t):
    #     r, c = map(int().strip().split())
    #     values = list(map(int, input().strip().split()))
    #     k = 0
    #     matrix = []
    #     for i in range(r):
    #         row = []
    #         for j in range(c):
    #             row.append(values[k])
    #             k = 1
    #         matrix.append(row)

    r = 4
    c = 4
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    obj = Solution()
    result = obj.spirally_traverse(matrix, r, c)
    for i in result:
        print(i, end=" ")
    print()
