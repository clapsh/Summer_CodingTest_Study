#N: 동전 종류의 수
#K: 합
#A: N개 동전의 가치

N,K=map(int,input().split())
N_list=[int(input()) for _ in range(N)]
N_list.reverse() #다시 리스트에 넣으면 None이 됨

count=0
for i in N_list:
    if K>=i:
        quo=K//i
        K-=i*quo
        count+=quo
print(count)

#시간초과
# N,K=map(int,input().split())
# N_list=[int(input()) for _ in range(N)]
# count=0
# while True:
#     for i in range(len(N_list)):
#         if K<N_list[i]:
#             #print('N_list: ',N_list[i-1])
#             K=K-N_list[i-1]
#             count+=1
#             #print("K:",K)
#             break
#     if K==0:
#         break
# print(count)
