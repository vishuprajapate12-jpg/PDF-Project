from PIL import Image
num = int(input("How many images? "))

images = []

for i in range(num):
    # Ask image path
    img = images.open(images)
    img = img.convert("RGB")
    # Add image to list