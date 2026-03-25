rows , cols = (5,5)

print([[0 for i in range(cols)]
for j in range(rows)])

def mostPonits(questions):
    n = len(questions)
    dp = [0]*(n+1)
    for i in range (n-1, -1,-1):
        points, brainpower = questions[i]
        next_index = i + brainpower + 1
        solve = points + (dp[next_index] if next_index <= n else 0)
        skip = dp[i +1]
        dp[i] = max(solve, skip)
    return dp [0]  


questions1 = [[3,2], [4,3], [4,4], [2,5]]
print(f"Example1: mostPoints(questions1)")

questions2 = [[1,1], [2,2],[3,3], [4,4], [5,5]]
print(f"Example 2 : mostPoints(questions2)")

questions3 = [[2,3], [4,4], [8,1], [0,10],[8,5]]
print(f"Example 3: mostPoints(questions3)")

questions4 = [[1,1], [2,2,], [3,3], [4,4,], [5,5], [6,6], [7,7], [8,8], [9,9],[10,10]]

print(f"Example 4: mostPoints(questions4)")