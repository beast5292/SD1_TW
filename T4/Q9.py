def menu(user_choice):
  if int(user_choice) == 1:
    print("1 selected")
  elif int(user_choice) == 2:
    print("2 selected")
  elif int(user_choice) == 3:
    print("3 selected")
  elif int(user_choice) < 1 or int(user_choice) > 4:
    print("Option not recognised")



running = False

while(not running):
  try:
    user_choice = input("Enter '1,2 or 3' for the option you prefer or '4' to quit..")
    if int(user_choice) == 1 or int(user_choice) == 2 or int(user_choice) ==3 \
        or int(user_choice) < 1 or int(user_choice) > 4:
      menu(user_choice)
    elif int(user_choice) == 4:
      print("Quit selected")
      running = True

  except ValueError:
    print("Enter integer")

  