print("Welcome to my Computer game!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okey! let's play ")

answer = input("What does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct")
else:
    print("Incorrect")


answer = input("What does GPU stand for ? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
else:
    print("Incorrect")


answer = input("What does RAM stand for ? ")
if answer.lower() == "random access memory":
    print("Correct")
else:
    print("Incorrect")


# incomplete still needs :

# point system ( to calculate the accumulated points ,....