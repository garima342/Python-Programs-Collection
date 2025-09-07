print("Welcome to this technical quiz game!")

playing = input("Ready to test your knowledge? ")

if playing!="yes":
    quit()
print("Okay! Let's play the game.")

score=0

answer = input("Which programming language is often associated with snake emojis but has nothing to do with reptiles? \n A) Java B) Python C) C++ D) Ruby\n")
if answer.lower()=="python":
    print("Correct!")
    score+=1
else:
    print("It's incorrect :(")

answer = input("Which of these is a frontend framework? \n A) Flask B) Django C) React D) NumPy \n")
if answer.lower()=="react":
    print("Correct!")
    score+=1
else:
    print("It's incorrect :(")

answer = input(" Which of these is not a valid Python data type? \n A) list B) tuple C) string D) floaty \n")
if answer.lower()=="floaty":
    print("Correct!")
    score+=1
else:
    print("It's incorrect :(")

answer = input("Which language is used to style web pages? \n A) HTML B) Python C) CSS D) SQL \n")
if answer.lower()=="css":
    print("Correct!")
    score+=1
else:
    print("It's incorrect :(")

print("Congratulations!!! You've successfully completed the quiz. Check out your score.")
print("You got",score,"questions correct.")
print("You got",score/4*100,"%")
print("Thank you for participating in the quiz!")