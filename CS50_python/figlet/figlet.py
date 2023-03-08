import sys
from pyfiglet import Figlet
import random

if len(sys.argv) == 1 or len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 3:
        if sys.argv[2] in fonts:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid Font")
    else:
        text = input("Input: ")
        rand = random.randint(0,len(fonts)-1)
        figlet.setFont(font=fonts[rand])
    print(figlet.renderText(text))
else:
    sys.exit("Usage: python figlet.py -f FONTNAME")