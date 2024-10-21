from  pyfiglet import Figlet
import sys
import random

figlet = Figlet()

available_fonts = figlet.getFonts()
font = random.choice(available_fonts) #to get random font
f =Figlet(font)

if len(sys.argv)==1:
    text = input("Input: ")
    print(f.renderText(text))
elif sys.argv[1] in ["-f","--font"]:
    if sys.argv[2] in available_fonts:
        text = input("Input: ")
        f =Figlet(font=sys.argv[2])
        print(f.renderText(text))
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")
