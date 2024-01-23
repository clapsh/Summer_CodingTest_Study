
 # 자리수 합 계산
def sumNumbers (n):
    value = 0
    for i in range(len(n)):
        a = n[i]
        if a.isdigit():
            value += int(a)
    
    return value

# 길이 계산
def str_len (my_dict):
    for key in my_dict:
        item_len = len(key)
        my_dict[key] = item_len
    
    return my_dict

n = int(input())
my_dict = {}
# 인풋 입력 받기
for _ in range(n):
    key = input()
    value = sumNumbers(key)
    my_dict[key] = value

# 1. 사전 순 정렬 
my_dict = dict(sorted(my_dict.items()))
# 2. 자리 수 합 정렬
my_dict = dict(sorted(my_dict.items(), key=lambda x : x[1]))
# 3. 길이 수 정렬
my_dict = str_len(my_dict)
my_dict = dict(sorted(my_dict.items(), key=lambda x : x[1]))

# 출력
for x in my_dict:
    print(x)