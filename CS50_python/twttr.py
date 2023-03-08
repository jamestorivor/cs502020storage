def main():
    word =  input("Input: ")
    for letter in shorten(word):
        print(letter, end="")


def shorten(word):
    shortened = ""
    for c in word:
        x = c.lower()
        if x not in ["a", "e", "i","o","u"]:
            shortened = shortened + c
    return shortened
    

if __name__ == "__main__":
    main()