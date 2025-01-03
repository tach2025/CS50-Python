def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return is_cond_1(s) and is_cond_2(s) and is_cond_3(s) and is_cond_4(s)


# All vanity plates must start with at least two letters
def is_cond_1(s):
    if len(s) < 2:
        return False
    else:
        return s[0:2].isalpha()


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def is_cond_2(s):
    return 2 <= len(s) <= 6


# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def is_cond_3(s):
    last_alph_pos = 0
    first_num_pos = len(s) + 1
    for i in range(len(s)):
        if s[i].isalpha():
            last_alph_pos = i
        elif first_num_pos == len(s) + 1:
            first_num_pos = i

    if first_num_pos == len(s) + 1:
        return True
    elif first_num_pos < last_alph_pos:
        return False
    elif s[first_num_pos] == '0':
        return False
    else:
        return True


# “No periods, spaces, or punctuation marks are allowed.”
def is_cond_4(s):
    return s.isalnum()


main()
