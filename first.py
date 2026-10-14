import sympy as sp

def Bisection(a, b, e):
    x = sp.symbols('x')
    equation  = sp.Eq(pow(x, 4) - 18 * pow(x, 2) + 6, 0)
    
    while abs(b - a) > 2*e:
        x0 = (a + b) / 2
        r = equation.subs(x, x0)

        if r == 0: 
            print(f"x = {x0}")
            return x0

        ra = equation.subs(x, a)
        fexp = (r * ra).expand()
        
        if r * fexp < 0: b = x0
        else: a = x0

Bisection(-1, 0, 0.01)

