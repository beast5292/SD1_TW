import random

def roll_dice ():
  dice_value = random.randint(1,6)
  return dice_value


#Initializing a variable to count the number of doubles
doubles_count = 0
for roll in range(100):
  dice_one_value = roll_dice()
  dice_two_value = roll_dice()
  
  if dice_one_value == dice_two_value:
    doubles_count += 1
print(f"out of 100 you rolled {doubles_count} doubles")