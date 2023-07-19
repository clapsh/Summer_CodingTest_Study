n = int(input())
for i in range(n):
    m = int(input())
    # 인풋 입력 받기 
    price = list(map(int, input().split()))
    max_profit = 0
    max_price = 0
    for idx in range(len(price)-1, -1, -1):
        curr_price  = price[idx]
        if  curr_price>= max_price:
            max_price = curr_price
        else:
            max_profit += (max_price - curr_price)
        
    print(max_profit)