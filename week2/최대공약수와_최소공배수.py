'''
최소공배수를 구할 때는 lcm을 써주면 된다. 
자세히 구현된 것을 보려면 코드를 뜯어보고 블로그에 정리해보자.
'''

import math as m
A, B = map(int, input().split())

print(m.gcd(A, B))
print(m.lcm(A, B))