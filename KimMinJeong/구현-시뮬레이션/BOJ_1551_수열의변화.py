#B[i]=A[i+1]-A[i]

size,change=list(map(int,input().split()))
text=list(map(int,input().split(',')))
for i in range(change):
    new_text=[]
    for x in range(size-1):
        new_text.append(text[x+1]-text[x])
    text=new_text
    size-=1
for i in range(size):
    if i!=size-1:
        print(text[i],end=',')
    else:
        print(text[i])
