#Fire Drill Monitor
room_number = input("what is the room number")


if "B" in room_number or "C" in room_number:
    print("That's an upper floor.")
else:
    print("That's a lower floor.")



number_of_students = int(input("how many students are in the room"))


if number_of_students <= 30:
  teacher = input("Is a teacher present")
  if teacher == "yes":
       print("Teacher is present")
  else:
       print("Teacher must be present. code red")
else:
   print ( "You should have more students")


exit_door = (input("Is the exit door clear?"))


if exit_door == "yes":
  print("good job, you found a rout")
else:
  print("Exit doors must be clear")


windows = (input("Are windows closed?"))


if windows == "yes":
  print("good job")
else:
  print("Lights should be off for proper evacuation")


Lights = (input("Are lights turned off?"))


if Lights == "yes":
  print("this is good for a proper evacuation")
else:
  print("Lights should be off for proper evacuation")

total = number_of_students + 1
print(f"Total people evacuating: {total}")


if teacher == "no":
   print("Fail:teacher is required")
elif exit_door == "no":
    print("Fail:exit door must be clear")
elif windows == "no":
   print("Fail:windows must be closed")
elif Lights == "no":
    print("Fail:lights must be off")
else:
    print("All conditions met, you may evacuate")


 
