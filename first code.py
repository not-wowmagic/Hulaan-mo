print("Hello sa quiz")

playing = input("Do you want to play ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for ")
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("Ano ")
if answer == "ano":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " Questions Correct!")
print("You got " + str((score / 2) * 100) + "%.")
