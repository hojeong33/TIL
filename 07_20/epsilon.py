#실수연산 시 눈에 보이는 것과 다른 숫자일 수 있음 
a=0.1+0.2
print(a)
print(a==0.3)

#방법 1)math
import math
print(math.isclose(a,0.3))

#방법 2)차이값
print(abs(a-0.3)<=1e-10)

#방법 3)sys
import sys
print(abs(a-0.3)<=sys.float_info.epsilon)
print(sys.float_info.epsilon) # 부동소수점 연산에서 반올림을 함으로써 발생하는 오차