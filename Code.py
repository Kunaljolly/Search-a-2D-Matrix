class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return
        for x in matrix:
            if target>=x[0] and target<=x[-1]:
                for y in x:
                    if y == target:
                        return True
                return False
        return False
        
