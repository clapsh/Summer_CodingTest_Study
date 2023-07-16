#사람: N
#돈 인출시간: P

N=int(input())
P=list(map(int,input().split()))
P.sort()
result=[]
sum=0
for i in P:
    sum+=i
    #print("sum: ",sum)
    result.append(sum)
#print("result: ",result)
answer=0
for i in result:
    answer+=i
print(answer)
