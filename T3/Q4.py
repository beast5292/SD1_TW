is_able_to_vote = False
is_able_to_drink = False

if is_able_to_vote and is_able_to_drink:
  print("You are an adult")

elif is_able_to_vote or not is_able_to_drink:
  print("You are a teenager")

else:
  print("You are not an adult")