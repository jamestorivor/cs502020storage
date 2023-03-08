def main():
    forty_two = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip()
    if forty_two == "forty two" or forty_two =="42" or forty_two =="forty_two":
        print("Yes")
    else:
        print("No")
    
    # match forty_two
    #     case "forty two" | "forty-two" | "42":
    #         print("Yes")
    #     case _:
    #         print("No")
    
main()