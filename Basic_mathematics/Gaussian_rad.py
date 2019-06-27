import math
import matplotlib.pyplot as plt


result = []
init, init2 = 0, 0
rad = 180 / math.pi
cnt = 0

for rep in range(360):

    result.append(init)
    print("[",cnt," rad]", init, "\t",init2, "\n")

    init += rad
    init %= 360
    init2 = int(init)
    cnt += 1



for o_rep in range(360):
    for i_rep in range(360):

        if(result[o_rep] == result[i_rep]):
            print(result[o_rep])
            break
