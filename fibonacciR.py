def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)







def main():
    a = int(input("enter which fibonacci index you want: "))
    b = fib(a)
    print(b)

if __name__ == "__main__":
    main()





