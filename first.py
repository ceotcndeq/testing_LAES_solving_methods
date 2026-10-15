import sympy as sp

def Bisection(a, b, e):
    x = sp.symbols('x')
    equation  = x**4 - 18*x**2 + 6
    
    while abs(b - a) > 2*e:
        x0 = (a + b) / 2
        res = equation.subs(x, x0)

        if res == 0: 
            return x0

        resa = equation.subs(x, a)
        fexp = res * resa
        
        if fexp < 0: b = x0
        else: a = x0
    
    print(f"x = {x0}")

Bisection(0, 1, 0.01)

