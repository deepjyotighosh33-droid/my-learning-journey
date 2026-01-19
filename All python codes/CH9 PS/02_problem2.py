import random

def game():
    print("You are playing the game")
    score = random.randint(1, 40)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open ("hiscore.txt", "w") as f:
            f.write("Hicore is " + str(score))
        
    return score

game()