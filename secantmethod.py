import math
system = input("Secant Method || [1] Iteration [2] Tolerance Error: ")

if system == "1":

    def secant_method(f_str, x0, x1, n):
        f = lambda x: eval(f_str.replace('x', str(x)))
        fx0 = f(x0)
        fx1 = f(x1)
        print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<10} {:<10}".format("Iteration", "Xn-1", "Xn", "f(Xn-1)", "f(Xn)", "Xn+1", "|xn+1 - Xn|"))

        for i in range(n):
            fx0 = f(x0)
            fx1 = f(x1)
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.10f} {:<10.6f} {:<10.6f}".format(i+1, x0, x1, fx0, fx1, x2, abs(x2-x1)))

            if abs(x2-x1) < 1e-6:
                cn = f(x2)
                print("f(Cn) =", cn)
                return x2
            x0 = x1
            x1 = x2

        print("Cn =", x2)
        return x2

    f_str = input("Enter function: ")
    x0 = float(input("Enter Xn-1: "))
    x1 = float(input("Enter Xn: "))
    n = int(input("Enter number of iteration: "))
    root = secant_method(f_str, x0, x1, n)
    print("(Cn) = {:<10.6f}".format(root))

elif system == "2":
    
    def secant_method(f_str, x0, x1, e):
        f = lambda x: eval(f_str.replace('x', str(x)))
        fx0 = f(x0)
        fx1 = f(x1)
        print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<10} {:<10} {:<10}".format("Iteration", "Xn-1", "Xn", "f(Xn-1)", "f(Xn)", "Xn+1", "|Xn+1 - Xn|", "< error"))
        n = 1
        while True:
            fx0 = f(x0)
            fx1 = f(x1)
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            print("{:<10} {:<10.6f} {:<10.6f} {:<10.6f} {:<15.10f} {:<10.6f} {:<10.6f} {:<10.6f}".format(n, x0, x1, fx0, fx1, x2, abs(x2-x1),e))

            if abs(x2-x1) < e: 
                cn = f(x2)
                print("f(Cn) =", cn)
                return x2
            x0 = x1
            x1 = x2
            n += 1

    f_str = input("Enter function: ")
    x0 = float(input("Enter Xn-1: "))   
    x1 = float(input("Enter Xn: "))
    e = float(input("Enter tolerance error: "))
    root = secant_method(f_str, x0, x1, e)
    print("Cn = {:<10.6f}".format((root)))






