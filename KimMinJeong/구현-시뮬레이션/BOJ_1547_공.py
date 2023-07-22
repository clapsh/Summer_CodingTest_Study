switch_count=int(input())
location=1
for i in range(switch_count):
    x,y=list(map(int,input().split()))
    if location==x:
        location=y
        continue
    elif location==y:
        location=x
print(location)
