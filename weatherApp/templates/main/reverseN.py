# your code goes here
l1=[int(item) for item in input().split()]
n,m=l1[0],l1[1]
numbers = [int(item) for item in input().split()]
l = []
for i in range(m):
    a = int(input())
    l.append(a)
count = 0
for i in range(m):
    reverseList=numbers[l[count]-1::-1]
    for j in range(len(reverseList)):
        numbers[j]=reverseList[j]
    count+=1
for i in range(len(numbers)):
    print(numbers[i],end=' ')



