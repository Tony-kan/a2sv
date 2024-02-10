
#function to check if the number 
#check if the number is even=can be diveded into 2 
#check if number > 2
def check_if_can_diveded(w):
    if w % 2 == 0 and w>2:
        print("YES")
    else:
        print("NO")


w = int(input())

check_if_can_diveded(w)