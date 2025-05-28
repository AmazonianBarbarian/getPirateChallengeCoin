from PIL import Image

# Open the image
img = Image.open("ItDontMatter.jpg")

x, y = img.size # Starting at the top left. image is 401x358px(Width(x),Height(y))

for i in range (0, y):
    for j in range (0, x):
        print(f"Coords ({j}, {i}): {img.getpixel((j, i))}")
        with open('imagePxData.txt', 'a') as text:
            if j == int(j - 1):
                text.write("\n")
            else:

                text.write(f"{img.getpixel((j, i))}, ")
    j = 0

text.close()
