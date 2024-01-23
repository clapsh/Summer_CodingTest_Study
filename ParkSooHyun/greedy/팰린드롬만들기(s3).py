str = input()

dic = {} #문자열을 알파벳 개수 (딕셔너리)
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for a in alph:
    dic[a] = 0
    
for ch in str:
     dic[ch] += 1

oddCnt = 0
oddAlph = 'a'
for key,value in dic.items(): # 홀수인 알파벳 카운트
    if value % 2 == 1 :
        oddCnt += 1
        oddAlph = key

if oddCnt > 1: # 홀수 개가 두 개 이상이면 팰린드롬을 만들 수 없음
    print ("I'm Sorry Hansoo")

else:
    sortedDic = dict(sorted(dic.items())) # 오름차순 정렬
    ans = ""
    for key,value in dic.items(): # 절반 문자열 만들기
        a = value // 2
        while (a):
            ans += key
            a -= 1
        
    reverseAns = ""   # 절반 대칭 문자열 만들기
    for ch in ans:
        reverseAns = ch + reverseAns
        
    if oddCnt == 1: #홀수가 하나인 경우
        ans += oddAlph

    ans += reverseAns # 절반 문자열 합치기
    print (ans)

        
    

         