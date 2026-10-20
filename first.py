import sympy as sp

x = sp.symbols('x')
equation  = x**4 - 18*x**2 + 6

def Bisection(a, b, e):

    while abs(b - a) > 2*e:
        x0 = (a + b) / 2
        res = equation.subs(x, x0)
        resa = equation.subs(x, a)
        fexp = res * resa

        print(f"a = {float(a):.4f}; b = {float(b):.4f}; "
              f"xn = {float(x0):.4f}; f(xn)*f(a) = {float(fexp):.4f}; "
              f"|bn - an| = {float(abs(b - a)):.4f}")

        if res == 0: 
            return x0
        
        if fexp < 0: b = x0
        else: a = x0
    
    print(f"x is {float(x0):.4f} with error margin {e}\n")


def Findx1(fixed, x0):
    fx0 = equation.subs(x, x0).evalf()
    fxfixed = equation.subs(x, fixed).evalf()
    
    if (fixed < x0): x1 = x0 - (fx0 * (x0 - fixed) / (fx0 - fxfixed))
    else: x1 = x0 - (fx0 * (fixed - x0) / (fxfixed - fx0))

    return x1

def Sacant(a, b, e):
    fxii = sp.diff(equation, x, 2)
    fxii_fx = fxii.subs(x, a) * equation.subs(x, a)
    
    if (fxii_fx > 0): 
        fixed = a
        x0 = b
    else:
        fixed = b
        x0 = a

    x1 = Findx1(fixed, x0)

    while abs(x1 - x0) > e:
        fx1 = equation.subs(x, x1).evalf()
        print(f"xn = {float(x0):.4f}, f(x1) = {float(fx1):.4f}, |xn-xn-1| = {float(abs(x1-x0)):.4f}")

        x0 = x1
        x1 = Findx1(fixed, x0)
    
    print(f"xn = {float(x0):.4f}, f(x1) = {float(fx1):.4f}, |xn-xn-1| = {float(abs(x1-x0)):.4f}")

    print(f"x is {float(x0):.4f} with error margin {e}\n")



a = 0
b = 1
e = 0.01
Bisection(a, b, e)
Sacant(a, b, e)

