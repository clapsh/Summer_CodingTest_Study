#잔돈
#500, 100, 50, 5, 1

money=int(input())
money=1000-money
change=[500, 100, 50, 10, 5, 1]
count=0
for i in change:
    if money>=i:
        num=money//i #몫 구하기
        money=money-i*num
        count+=num
print(count)
