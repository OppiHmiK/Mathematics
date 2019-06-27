print("이 프로그램은 완전수인지 판별하는 프로그램입니다.")
n = input("판별하고 싶은 수를 입력하십시오. : ")

inn = int(n)
i = 1; s = 0
m = int(inn/2)
        
if inn == 1:
    print("이 수는 완전수가 아닙니다.")

else:
    while i<=m:

        R = inn%i
        if R == 0:
             s = s+i

        i = i+1
        continue

    if s == inn:
        print("이 수는 완전수입니다.")
    else:
        print("이 수는 완전수가 아닙니다.")
        
        

        
