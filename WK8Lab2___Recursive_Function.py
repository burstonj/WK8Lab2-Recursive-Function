def fib(n):#Fibonacci sequence fuction
    if n == 0:
        return 0#starts at 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2) #has to call the fib funtion twice to increase the number

def main():
    for i in range(16):#16 is the end for this lab, but can be any number.
        print(fib(i), end=", ")
    print("...")

if __name__ == "__main__":
    main()


