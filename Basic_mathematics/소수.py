import math as mt

print("n에서 m까지 소수를 찾아주는 프로그램입니다.")
n = int(input("n값을 입력해주세요."))
m = int(input("m값을 입력해주세요."))

if n>m:
    max = n; min = m

else:
    max = m; min =n
    
p = 2

while min<=max:

    sqt = int(mt.sqrt(max))

    j = 1
    
    while j > sqt:
        R = min%j

        if R != 0:
            j = j+1

        p = min
        print(p)
    min = min+1
    print(p)
    
