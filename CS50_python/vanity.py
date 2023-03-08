
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    counter = 0
    if not (2 <= len(s) <= 6):
        return False
    elif not (s.isalnum()):
        return False
    elif not (s[0:2].isalpha()):
        return False
    elif len(s) > 2:
        for c in s:
            if c.isdigit():
                if c == "0" and counter == 0 :
                    return False
                else:
                    counter += 1
    if counter > 0:
        if s[len(s)-1].isalpha():
            return False
    return True
if __name__=="__main__":
    main()