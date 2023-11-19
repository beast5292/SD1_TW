#part a

for number in range(3) :
  print("-------------------------------------------")
  print("Outer loop iteration " + str(number))
  # Inner loop
  for another_number in range(4):
    print("****************************")
    print("In inner loop iteration " + str(another_number))

""" Ans) In this code block the inner loop iterates 4 times (0-3) per
each iteration of the outer loop. The outer loop iterates 3 times (0-2)
"""

#part b

for x in range(1,4): # print 3 rows
  for y in range(1,4): # 3 asterisks a row
    print('*', end='')
  print()

""" Ans) In this code block the inner loop iterates 3 times (1-3) 
per each iteration (1-3) of the outer loop.The inner loop prints 
3 asterisks consecutively and then a new line is printed before the outer loop runs again"""

#part c

for outer in range(4):
  for inner in range(outer):
    print("*",end="")
  print()