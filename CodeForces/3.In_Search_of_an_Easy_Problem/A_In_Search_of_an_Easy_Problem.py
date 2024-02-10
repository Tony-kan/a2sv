#get number of pple as input n
#get a list of 0 & 1's

def check_problem_difficulty(list1):
    if 1 in list1:
        return "HARD"
    else:
        return "EASY"

n = int(input())

list1 =(map(int, input().split()))


print(check_problem_difficulty(list1))
  

