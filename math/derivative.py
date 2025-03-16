import sympy

x = sympy.Symbol('x', real=True)
f = x**3 + 2*x
fprime = sympy.diff(f, x)   # Symbolic derivative: 3x^2 + 2
result = fprime.subs(x, 1)  # Evaluate at x=2
print(result)               # 14
