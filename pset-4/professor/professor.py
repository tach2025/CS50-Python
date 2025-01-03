import random


def main():
    n = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        for j in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == x + y:
                    score += 1
                    break
                else:
                    raise Exception
            except:
                print("EEE")
                continue
        else:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")


def get_level():
    valid_levels = [1, 2, 3]
    while True:
        try:
            n = int(input("Level: "))
            if n not in valid_levels:
                raise Exception
        except:
            continue
        else:
            return n


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
