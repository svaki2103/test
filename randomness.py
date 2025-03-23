import random

def roll_random(key):

    mystery = []
    randomness = ""

    for i in range(len(key)):
        mystery.append(0)
        mystery[i] = ord(key[i]) ^ 1337

        randomness += str(mystery[i])

    random.seed(int(randomness))
    roll = random.randint(1, 1338) * int(randomness)

    return roll

def check_random(randomness):
    if randomness == 440043684378039723076352440044228301237163396422837803364390842283364378037483940371636524228378037483940422830123716339642283588374837163460422835243428422838443684378033004228301237163396336442283556378037483940333231360:
        print("How did you break out of the randomness??")
    else:
        print("Try again.")

if __name__ == "__main__":

    key = input("What's the key?\n")

    randomness = roll_random(key)
    check_random(randomness)