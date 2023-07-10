while True:
    try:
        s, t=input().split()
        index_s=0 #s의 위치
        count=0 #s가 t에 모두 있는지 확인하는 용도
        for i in range(len(t)):
            if t[i]==s[index_s]:
                index_s+=1
                count+=1
                if count==len(s): #s가 t의 부분 문자열인 경우
                    count=-1
                    break
        if count==-1:
            print("Yes")
        else:
            print("No")
    except EOFError:
        break
