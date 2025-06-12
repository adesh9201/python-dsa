# Problem statement
# Sam is making a Triangular painting for a maths project.

# An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers starting from 1.

# For every value of ‘N’, help sam to print the corresponding N-dimensional Triangle.

# Example:
# Input: ‘N’ = 3

# Output: 
# 1
# 1 2 
# 1 2 3
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1  <= N <= 25
# Time Limit: 1 sec
# Sample Input 1:
# 3
# Sample Output 1:
# 1
# 1 2 
# 1 2 3
# Sample Input 2 :
# 1
# Sample Output 2 :
# 1


#  use class Solution:

print("Using class Solution:")

class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(j, end=' ')
            print()  

sol = Solution()
sol.printTriangle(3)
# Sample Output :
# 1
# 1 2 
# 1 2 3





#  use function nTriangle:

print("\nUsing function nTriangle:")

def nTriangle(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
nTriangle(3)


# Sample Output:
# 1
# 1 2
# 1 2 3

