from src.findrunnerup_problem.util import runner_up_score

# Input
n = int(input())
scores = list(map(int, input().split()))
print(runner_up_score(scores))  # call the function
