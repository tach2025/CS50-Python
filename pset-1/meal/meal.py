# Main function
def main():
    # Prompt user to enter time
    time_str = input("What time is it? ").strip()
    # Get the time in float
    time_float = convert(time_str)
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")


def convert(time):
    if time.endswith("m."):
        h_m, am_pm = time.split()
        h, m = h_m.split(":")
        h = float(h)
        m = float(m)
        if am_pm.startswith("p."):
            h += 12
        return h + m / 60
    else:
        h, m = time.split(":")
        h = float(h)
        m = float(m)
        return h + m / 60


if __name__ == "__main__":
    main()
