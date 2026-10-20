# testing_LAES_solving_methods

! the title of the project is a bit misleading, as so far it's dedicated to implementing 
methods that search for approximate solutions to equations within a specified range, not systems

!! and i'm sorry to those who decided to read this readme, as i intend to use it as a journal mostly. 
until the project is sufficient enough to have a readme at all, hehe

2026/10/14
it's an educational project designed to help me understand 4 numeric methods for solving algebraic linear equations.
methods i want to implement:
- bisection
- fixed-point iterations
- sacant method
- Newton's method

my python knowledge is not very extensive. i'll be using
SymPy library for calculations

2026/10/15
Bisection method works for now, the results of the positive test-cases map to the manual calculations. 
there's a lot to do to make this one any useful in the real world, of course, but for now i intend to implement 
the most trivial dumbdown versions of all four methods, otherwise i'll get stuck

2026/10/20-21
so, i managed to implement sacant method! i spent two hours or so, which isn't much, but i went through
all stages of grief while doing it. key points of my work today:
- it consists of two functions. Findx1() is needed since some parts of the formula change depending on the fixed point
- there's a little problem with print, as it doesn't print out the last iteration of the method inside the loop;
i had to write it down explicitly, but it's fine, i hope i won't forget it, as it's late into the night when
i'm writing this
- added float() with precision 4f inside print() to make the output less messy than it had been. 4f because
the teacher who gave us this assignment asked for this precision

actually, the solution is simple, as it always is, but i went thousands circles around it before realizing it.
i'm happy anyway

the next method will be Newton's method, most likely