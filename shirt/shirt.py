import sys
from os.path import splitext
from PIL import Image,ImageOps

if len(sys.argv) == 3:
        extensions = [".jpg", ".jpeg", ".png"]
        extension1 = splitext(sys.argv[1])
        extension2 = splitext(sys.argv[2])
        if extension1[1] == extension2[1] and extension1[1] in extensions:
                try:
                        BeforeImage = Image.open(sys.argv[1])
                except FileNotFoundError:
                        sys.exit("File not found")
        #Image.open
                shirt = Image.open("shirt.png")
                size = shirt.size
        #ImageOps.fit
                muppet = ImageOps.fit(BeforeImage,size)
        #Image.paste
                muppet.paste(shirt, shirt)
        #Image.save
                muppet.save(sys.argv[2])

        elif extension1[1].lower() != extension2[1].lower():
                sys.exit("Input and output have different extensions")
        else:
                sys.exit("Wrong Extension")

elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
else:
    sys.exit("Invalid input")