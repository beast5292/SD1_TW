
n = input("Enter a number greater than 100 ")

try:

  if int(n) <= 100:
    print(f"{n} is less than 100")
  else:
    print(f"{n} is greater than 100")

except:
  print("There is a value error")

