class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(matrix)):
            minimum = min(matrix[i])
            for j in range(len(matrix[i])):
                if matrix[i][j] == minimum:
                    maximum = True
                    for k in range(len(matrix)):
                        if matrix[k][j] > matrix[i][j]:
                            maximum = False
                            break
                    if maximum:
                        result.append(matrix[i][j])
        return result
