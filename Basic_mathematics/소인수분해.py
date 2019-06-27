print("이 프로그램은 입력하신 수의 소인수 분해 결과를 출력하는 프로그램입니다.")
n = int(input("2 이상의 수를 입력하십시오. : "))
lis = []; p = 2; i=0

if n<2:
    print("2이상의 수를 입력하십시오.")

else:

    while p<=n:
        if n%p == 0:
            i = i+1
            lis.append(p)
            n=n/p

        else:
            p = p+1

    if i == 1:
        print("이 수는 소수입니다.")
    else:
        for t in (0,i-1):
            num = str(lis[t])
        print("당신이 입력하신 수의 소인수 분해 결과는 "+num+"입니다.")   
