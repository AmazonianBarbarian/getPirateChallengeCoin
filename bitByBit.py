from PIL import Image

# Open the image
img = Image.open("ItDontMatter.jpg")

x, y = 0, 0 # Starting at the top left. image is 401x358px(Width(x),Height(y))
pixel_value = img.getpixel((x, y))
print(f"Pixel value for({x}, {y}): {pixel_value}")
for y in range (0, 358):
    for x in range (0, 401):
        print(f"Coords ({x}, {y}): {pixel_value}")
        with open('imagePxData.txt', 'a') as text:
            if x == 400:
                text.write("\n")
            else:    
                text.write(f"{pixel_value}, ")
    x = 0

text.close()
