from PIL import Image

RGB_BLACK = (0, 0, 0)
RGB_DIFFERENCE = 60


def is_rgb_value_similar(value1, value2):
    if (abs(value1[0] - value2[0]) <= RGB_DIFFERENCE and
        abs(value1[1] - value2[1]) <= RGB_DIFFERENCE and
        abs(value1[2] - value2[2]) <= RGB_DIFFERENCE):
        return True
    return False


im = Image.open('../image/image.jpg') # Can be many different formats.
pix = im.load()
x,y = im.size
print(im.size)  # Get the width and hight of the image for iterating over
mid = x / 2
for i in range(y):
    #print(str(i) + " " + str(pix[mid,i]))
    if is_rgb_value_similar(pix[mid,i], RGB_BLACK):
        print("This pixel is black: " + str(i))
