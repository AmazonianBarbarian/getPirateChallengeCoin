from PIL import Image

# Open the image
img = Image.open("/home/astridlr/pythonProjects/pirateSoftwareDecrypt/PirateChallCoin/screenshotFile/screenshotOrigin.png")

x, y = img.size # Starting at the top left. image is 401x358px(Width(x),Height(y))

for i in range (0, y): # Looping through the rows.
    for j in range (0, x): # Looping through the columns.
        print(f"Coords ({j}, {i}): {img.getpixel((j, i))}") # { j is x, i is y }
        with open('imagePxData.txt', 'a') as text:
            text.write(f"{img.getpixel((j, i))}, ")
    with open('imagePxData.txt', 'a') as text:
        text.write("\n")
    j = 0

text.close()
