from PIL import Image
from PIL import ImageOps
import sys
import os 

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            ext1 = os.path.splitext(sys.argv[1])
            ext2 = os.path.splitext(sys.argv[2])
            if ext1[1] and ext2[1] not in ('.jpg', '.png', '.jpeg'):
                print(ext1[1])
                print(ext2[1])
                sys.exit("invalid input")
            elif ext1[1] != ext2[1]:
                sys.exit("Input and output have different extensions")
            else:
                with Image.open("shirt.png") as shirt:
                    size = shirt.size
                    with Image.open(sys.argv[1]) as before:
                        background = ImageOps.fit(before, size)
                        background.paste(shirt, (0,0), shirt)
                        background.save(sys.argv[2])
                
    except FileNotFoundError:
        sys.exit("File does not exist")
    
if __name__ == "__main__":
    main()    