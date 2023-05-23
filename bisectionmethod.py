import math 

system = input('Bisection Method || [1] Tolerance Error [2] Iteration: ')

if system == "1":
    def bisection_method(f_str, a, b, e):
        fa = eval(f_str.replace('x', str(a)))
        fb = eval(f_str.replace('x', str(b)))
       
        iteration = 1
        print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<10} {:<10}".format("Iteration", "a", "b", "c", "f(c)", "|a-b|", "< error" ))
        print("-" * 85)
        while abs(a - b) > e:
            c = (a + b) / 2
            fc = eval(f_str.replace('x', str(c)))
            print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.10f} {:<10.6f} {:<10.6f}".format(iteration, a, b, c, fc, abs(a - b), e))
            if fc == 0:
                return c
            elif fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
            iteration += 1
        
        root = (a + b) / 2
        print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.10f} {:<10.6f} {:<10.6f}".format(iteration, a, b, root, eval(f_str.replace('x', str(root))),abs(a - b), e))
        print('Cn = ',root)
        print('f(Cn) = ', fc)
        return root

    f_str = input("Enter your function: ")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    e = float(input("Enter the tolerance: "))
    
    root = bisection_method(f_str, a, b,e)

elif system == "2":

    def bisection_method(f_str, a, b, n):
        fa = eval(f_str.replace('x', str(a)))
        fb = eval(f_str.replace('x', str(b)))

        if fa * fb >=0:
            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Iteration", "a", "b", "Cn", "f(cn)", "|a-b|"))
        else:
            c = (a+b) / 2
            fc = eval(f_str.replace('x', str(c)))
            e = abs(a-b)
            print ("{:<10} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}".format(0, a, b, c, fc, e))
            if fc == 0:
                return c
            
        for i in range (n):
            c = (a+b) / 2
            fc = eval(f_str.replace('x', str(c)))
            e = abs(a-b)

            print ("{:<10} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}".format(i+1, a, b, c, fc, e))

            if fc == 0:
                return c
            
            if fa * fc <0:
                b = c
            else:
                a = c
                fa = fc

        root = (a+b)/2
        print('Cn = ', c)
        print('f(Cn) = ', fc)
        return root

    f_str = input("Enter your function: ")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))   
    n = int(input("Enter number of iteration: "))
    root = bisection_method(f_str, a, b,n)
