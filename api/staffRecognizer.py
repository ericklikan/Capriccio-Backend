from PIL import Image
from notesRecognizer import GripPipeline

RGB_BLACK = (0, 0, 0)
RGB_DIFFERENCE = 100

PIXEL_DIFFERENCE = 10


def is_rgb_value_similar(value1, value2):
    if (abs(value1[0] - value2[0]) <= RGB_DIFFERENCE and
        abs(value1[1] - value2[1]) <= RGB_DIFFERENCE and
        abs(value1[2] - value2[2]) <= RGB_DIFFERENCE):
        return True
    return False


def find_staff_coordinates(image :str) -> list:
    im = Image.open(image)
    pix = im.load()
    x, y = im.size
    mid = x / 2

    line_count = 0
    staff_coordinates = []

    for i in range(y):

        #print(pix[mid,i])
        if is_rgb_value_similar(pix[mid, i], RGB_BLACK):
            y_coord = i
            if line_count == 0 or abs(y_coord - staff_coordinates[line_count - 1]) > PIXEL_DIFFERENCE:
                staff_coordinates.append(y_coord)
                line_count += 1

    return staff_coordinates

print(find_staff_coordinates('../image/arpeggio.jpg'))
#print(find_staff_coordinates('../image/image.jpg'))
print("output")
gripPipeline = GripPipeline()
#gripPipeline.process('../image/image.jpg')
gripPipeline.process('../image/arpeggio.jpg')