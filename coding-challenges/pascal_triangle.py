# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        
        for i in range(numRows):
            if i == 0:
                pascal_triangle.append([1])
                
            elif i == 1:
                pascal_triangle.append([1,1])
                
            else:
                n = 1
                sm = [1]

                for j in range(len(pascal_triangle[i-1])-1):
                    sm.append(pascal_triangle[i-1][j] + pascal_triangle[i-1][j+1])
                
                sm.append(1)                
                pascal_triangle.append(sm)
                
        return pascal_triangle
