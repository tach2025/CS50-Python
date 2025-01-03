import random

while True:
    try:
        n = int(input("Level: "))
        if n < 0:
            raise Exception
        rand_int = random.randint(1, n)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess < 0:
                    raise Exception
                if guess < rand_int:
                    print("Too small!")
                    continue
                elif guess > rand_int:
                    print("Too large!")
                    continue
                else:
                    print("Just right!")
            except:
                continue
            else:
                break
    except:
        continue
    else:
        break
