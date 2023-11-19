mark = input("enter your marks ")

try:
  if int(mark) <= 40:
    print(f"failed")
  else:
    print(f"{mark} means you passed")

except:
  print("there is an error") 