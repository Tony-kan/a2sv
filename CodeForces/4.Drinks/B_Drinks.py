#get number of orange drinks in refrigerator as n
#get the proportion for each as a list1
#format the output to 12 decimal places

def percentage_calculator(n,list1):
    total = sum(list1)/n

    return "{:.12f}".format(total)


n=int(input())
list1 =(map(int,input().split()))

print(percentage_calculator(n,list1))









n