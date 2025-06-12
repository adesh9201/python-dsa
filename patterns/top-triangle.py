# Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.

# Help Geek build a star pattern.

# Example 1:

# Input: 5
# Output:
# * * * * *
# * * * * 
# * * * 
# * *  
# * 
# Example 2:

# Input: 3
# Output:
# * * * 
# * *  
# * 
# Your Task:
# You don't need to input anything. Complete the function printTriangle() which takes an integer n  as the input parameter and prints the pattern.

# Expected Time Complexity: O(n2).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1<= n <= 100






#  use class Solution:
print("Using class Solution:")

class Solution:
    def printTriangle(self, N):
        for i in range(N, 0, -1):
            print("* " * i) 

sol = Solution()
sol.printTriangle(5)
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
# *






#  use function nTriangle:

print("\nUsing function nTriangle:")

def nTriangle(n: int) -> None:
    for i in range(n, 0, -1):
        print("* " * i)
        
nTriangle(5)
# Output:
# * * * * *
# * * * *
# * * *
# * *
# * *
# *
