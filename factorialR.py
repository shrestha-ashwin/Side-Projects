def fact(n):
    if n == 0 or n == 1:
        return 1 
    return n * fact(n-1)


def main():
    while True:
        a = input("Enter an integer: ")
        try: 
          a = int(a)
        except Exception as e:
            print("Error: ",e)
            continue
        break
    b = fact(a)
    print("The factorial of {0} is {1}".format(a,b))

if __name__ == "__main__":
    main()

