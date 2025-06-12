# Problem statement
# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N/2-dimensional forest.

# Example:
# Input:  ‘N’ = 3

# Output: 
# * 
# * *
# * * *


#   use class Solution:
print("Using class Solution:")

class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            print("* " * i)
sol = Solution() 
sol.printTriangle(3) 
# Output: 
# * 
# * *
# * * *         
            
            
            
            
print("\nUsing function nForest:")
#   use function nForest:

def nForest(n: int) -> None:
    for i in range(1, n + 1):
        print("* " * i)
        
nForest(3)
# Output:
# *
# * *
# * * *