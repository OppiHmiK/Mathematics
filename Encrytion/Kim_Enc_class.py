import re
import math as mt
import time as t
import random as rand

class Kim_number:

    def __init__(self):
        self.seq = []

    def is_prime(self, in_num):

        sqrt = int(mt.sqrt(in_num))
        isPrime = 1

        if in_num < 2:
            isPrime = 0

        else:

            for rep in range(2, sqrt + 1):

                res = in_num % rep
                if res == 0:
                    isPrime = 0
                    break

            return isPrime

    def get_prime(self, in_num):

        pri_lis = []
        for rep in range(1, in_num + 1):

            if self.is_prime(rep):
                pri_lis.append(rep)

        return pri_lis

    def gcd(self, in_num1, in_num2):

        if in_num1 > in_num2:

            max = in_num1
            min = in_num2

        else:

            max = in_num2
            min = in_num1

        while True:

            res = max % min
            max = min
            min = res

            if res != 0:
                continue
            return max

    def facto(self, in_num):

        mul = 1
        for rep in range(1, in_num + 1):
            mul = mul*rep
        print(mul)

    def numerical_diff(self, func):
        delta = 1e-6
        return (func(x+delta) - func(x-delta)) / (2*delta)

class Kim_RSA(Kim_number):

    def gen_key(self, in_num):

        c_time = t.ctime()
        rand.seed(c_time)

        primes = rand.sample(self.get_prime(in_num), 2)
        pri1 = primes[0]
        pri2 = primes[1]

        pu_key = {}
        pr_key = {}
        enc = 0
        dec = 0

        n = pri1 * pri2
        eul_n = (pri1 - 1) * (pri2 - 1)

        for rep in range(2, eul_n):

            if self.gcd(rep, eul_n) == 1:
                enc = rep
                break

        for rep in range(2, eul_n):

            if enc*rep % eul_n == 1:
                dec = rep
                break

        pu_key['enc'] = enc; pu_key['n'] = n
        pr_key['dec'] = dec; pr_key['n'] = n

        return pu_key, pr_key

class Kim_backpack(Kim_number):

    def bin_trim(self, in_bin):

        in_bin = in_bin[2:] # NOTE : 2진수로 변환하였을 때, 0b가 붙는 것을 제거해줌.
        return in_bin

    def message(self, in_message):

        with open(in_message) as data:

            cha2int = [] # NOTE : 평문을 숫자로 변환하여 저장해줄 리스트
            self.message = ''  # NOTE : 평문을 2진 코드로 변환한 결과를 저장할 문자열
            mul = 1; sum = 0
            
            # NOTE : 데이터 전처리 과정
            contents = data.read() # NOTE : 데이터 불러오기
            contents = contents.upper() # NOTE : 소문자를 대문자로 바꿔줌.
            contents = contents.replace(" ", "") # NOTE : 공백 제거.
            contents = contents.replace("\n", "") # NOTE : 줄 띄우기 제거.
            contents = contents.replace("'","") # NOTE : 작은 따옴표 제거.
            contents = re.sub('[-.,"!?:]', "", contents) # NOTE : 정규표현식으로 특수문자들 제거.

            # NOTE : 문자의 아스키 코드 값이 65를 넘으면 65를 빼줌.
            for rep in contents:
                if ord(rep) > 64:
                    cha2int.append(ord(rep) - 64)

            # NOTE : 복호화 할때 5글자의 2진코드로 끊어서 할 수 있도록,
            #        2진코드로 변환한 결과의 길이가 5가 아니면 모자란 만큼 앞에 0을 추가하고, 모든 이진코드를 하나로 붙임.
            for rep in range(0, len(cha2int)):

                mesg = list(self.bin_trim(bin(cha2int[rep])))
                if len(mesg) != 5:
                    for rep2 in range(0, 5-len(mesg)):
                        mesg.insert(rep2, '0')

                mesg = ''.join(mesg)
                self.message = self.message + mesg

            # NOTE : 초월 증가 수열인 2의 거듭제곱승을 모아둔 리스트
            for rep in range(1, len(self.message) + 1):
                mul *= 2
                self.seq.append(mul)

            # NOTE : 초월 증가 수열의 합
            for rep in range(0, len(self.message)):
                sum += self.seq[rep]

            return sum , len(self.seq)

    def get_nums(self, in_message):

        res, seq_sum = self.message(in_message)

        vec = [rep for rep in range(seq_sum + 10000) if rep > seq_sum + 1] # NOTE : 초월수열의 합보다 큰 수들을 모아둔 리스트.
        pr_key1 = rand.sample(vec, 1) # NOTE : 초월수열의 합보다 큰 수들을 모아둔 리스트에서 임의로 하나를 추출하여 비밀키 중 하나로 보관.

        for rep in range(vec[0], pr_key1[0]):
            if self.gcd(rep, pr_key1[0]) == 1: # NOTE : 임의로 추출한 비밀키와 서로소인 수를 임의로 하나 골라서 두번째 비밀키로 보관.
                pr_key2 = rep

        return pr_key1[0], pr_key2

    def gen_key(self, in_message):

        self.pu_key = []

        self.pr_key1, pr_key2 = self.get_nums(in_message)

        for rep in range(1, self.pr_key1):
            if rep*pr_key2 % self.pr_key1 == 1:
                self.dec_key = rep

        for rep in range(0, len(self.seq)):
            b = self.seq[rep] * pr_key2 % self.pr_key1 # NOTE : 초월증가 수열의 각각의 원소들과 두번쨰 비밀키 값을 곱해 첫번째 비밀키 값으로 나누어줌.
            self.pu_key.append(b) # NOTE : 위의 설명과 같은 값을 모아둔 리스트들을 공개키로써 공개함.

        return len(self.pu_key), self.dec_key

    def enc(self, in_message):

        m_len, dec_key= self.gen_key(in_message)
        self.cryp = 0

        for rep in range(0, m_len):

            self.cryp = self.cryp + int(self.message[rep])*self.pu_key[rep] # NOTE : 평문을 2진 코드로 변환한 값과 공개키의 원소를 내적하여 암호화 함.

        int_mesg = self.cryp*dec_key % self.pr_key1

        return self.cryp, int_mesg

    def dec(self, in_message):

        seq = self.seq
        int_mesg = self.enc(in_message)[1]
        mesg = []

        for rep in range(len(seq)-1, -1, -1):
            if seq[rep] > int_mesg:
                mesg.append('0')
            else:
                int_mesg -= seq[rep]
                mesg.append('1')

        mesg = ''.join(mesg)


        return mesg

kim = Kim_backpack()
print(kim.dec("Hae.txt"))

