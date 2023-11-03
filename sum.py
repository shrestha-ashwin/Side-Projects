def sum(n):
   if n ==0:
      return 0
   return n + sum(n-1)




def main():
    while True:
      a = input("enter a number: ")
      try:
         a = int(a)
      except Exception as e:
         print("Error: ",e)
         continue
      break
    b = sum(a)
    print("The sum of {0} consecutive numbers starting from 0 is {1}".format(a,b))







if __name__ == "__main__":
    main()