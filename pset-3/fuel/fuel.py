while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        fuel = round(x * 100 / y)
        if fuel >= 99:
            print("F")
        elif fuel <= 1:
            print("E")
        else:
            print(f"{fuel}%")
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        break
