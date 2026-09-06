from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

# get a list of available fonts
font_names = figlet.getFonts()

length = len(sys.argv)
if length <= 3:
    match length:
        case 1:
            text = input("Input: ")
            font = random.choice(font_names)
            figlet.setFont(font=font)
            print("Output: \n", figlet.renderText(text))
        case 3:
            flag = sys.argv[1]
            font = sys.argv[2]
            if (flag == "--font" or flag == "-f") and (font in font_names):
                text = input("Input: ")
                figlet.setFont(font=font)
                print("Output: \n", figlet.renderText(text))
            else:
                print("Invalid usage")
                sys.exit(1)
        case _:
            print("Invalid usage")
            sys.exit(2)
