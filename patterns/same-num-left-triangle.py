# Geek is very fond of patterns. Once, his teacher gave him a  pattern to solve. He gave Geek an integer n and asked him to build a pattern.

# Help Geek to build a pattern.

 

# Example 1:

# Input: 5

# Output:
# 1
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5



# Your Task:

# You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.

# Constraints:

# 1<= N <= 20




#   use class Solution:

print("Using class Solution:")

class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            print((str(i) + ' ') * i, end='')  # prints i repeated i times with space
            print()  # newline after each row

sol = Solution()
sol.printTriangle(5)
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5






#   use function nTriangle:

print("\nUsing function nTriangle:")

def nTriangle(n: int) -> None:
    for i in range(1, n + 1):
        print((str(i) + ' ') * i, end='')  # prints i repeated i times with space
        print()  # newline after each row
        
nTriangle(5)
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

