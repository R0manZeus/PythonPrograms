print("Welcome to Treasure Island\nChoose your next step. . .carefully")
direction = input("Where would you like to go? Right or Left\n").lower()
if direction == "left":
  sw = input("You come across a lake with boats far from shore, what do you do? Swim or Wait\n").lower()
  if sw == "wait":
    door = input("You come across 3 doors, which door would you like to us? Blue, Green or Yellow\n").lower()
    if door == "blue":
      print("Wrong door, fuck off!")
    if door == "green":
      print("You got attacked by faceless monsters")
    elif door == "yellow":
      print("You win!")
  else:
    print("You got attacked by fucking crocodiles")
else:
  print("Game Over")

