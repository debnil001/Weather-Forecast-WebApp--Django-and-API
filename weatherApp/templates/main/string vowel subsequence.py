# from itertools import *
def isvowel(s):
    l=[]
    for i in s:
        if i=='a' or i=='e' or i=='i'or i=='o'or i=='u':
            l.append(i)
    return l
# def makeCombination(s):
#     comblist=[]
#     finallist=[]
#     for i in range(1,len(s)+1):
#         comblist.append(list(combinations(s,i)))
#     for i in comblist:
#         for j in i:
#             s=''.join(j)
#             finallist.append(s)
#     return finallist
# def match(s1,s2):
#     maxlen=0
#     for i in s1:
#         if i in s2:
#             if len(i)>maxlen:
#                 maxlen=len(i)
#     return maxlen
# s1=isvowel(input())
# s2=isvowel(input())
# finallist1=makeCombination(s1)
# finallist2=makeCombination(s2)
# print(match(finallist1,finallist2))

test_str=''.join(isvowel("vowelpunish"))
res=[test_str[i:j] for i in range(len(test_str)) for j in range(i+1,len(test_str)+1)]
print(res)