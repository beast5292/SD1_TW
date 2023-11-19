import time

user_choice = input("Enter the number of stars you want as an integer..")

for star in range(int(user_choice)):
  print("*")
  time.sleep(0.5)