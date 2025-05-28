from PIL import Image

# Open the image
img = Image.open("ItDontMatter.jpg")

x, y = img.size # Starting at the top left. image is 401x358px(Width(x),Height(y))

for y in range (0, 358):
    for x in range (0, 401):
        print(f"Coords ({x}, {y}): {img.getpixel((x, y))}")
        with open('imagePxData.txt', 'a') as text:
            if x == 400:
                text.write("\n")
            else:

                text.write(f"{img.getpixel((x, y))}, ")
    x = 0

text.close()
