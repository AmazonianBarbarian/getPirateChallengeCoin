#This is a script meant to analyze an image pixel by pixel.

from PIL import Image

# Open the image
img = Image.open("/home/astridlr/pythonProjects/pirateSoftwareDecrypt/PirateChallCoin/screenshotFile/screenshotOrigin.png")

x, y = img.size # Starting at the top left. image is 401x358px(Width(x),Height(y))
text = open('imagePxData.txt', 'w')
for i in range (0, y): # Looping through the rows.
    for j in range (0, x): # Looping through the columns.
        value = img.getpixel((j, i)) # Used for efficiency. Not gonna call the same function more times than I need to.
        print(f"Coords ({j}, {i}): {value}") # { j is x, i is y }
        text.write(f"{value}, ")
    text.write("\n")

text.close()
img.close()
