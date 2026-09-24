class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, columns = len(text1) + 1, len(text2) + 1

        dp = [[0 for j in range(columns)] for i in range(rows)]

        for i in range(1, rows):
            for j in range(1, columns):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

#         C   A   T
#     0   0   0   0
# C   0   1   1   1
# R   0   1   1   1
# A   0   1   2   2
# B   0   1   2   2   
# T   0   1   2   3