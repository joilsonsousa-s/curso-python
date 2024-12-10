soma = lambda x, func:x + func(x)
res = soma(2, lambda x:x + 5)
print(res)

"""
soma = lambda x, func:x + func(x)
res = soma(2, lambda x:x * x)
print(res)
"""

"""
soma = lambda x, func:x + func(x)
print(soma(7, lambda x:2 * 35))
"""

"""
print((lambda a, b:a + b)(4,7))
"""

"""soma = lambda a, b: a + b
mult = lambda a, b, c: (a + b) * c
print(soma(70,7))
print(mult(5,5,2))"""