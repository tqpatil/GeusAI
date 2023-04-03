import cv2
import numpy
from matplotlib import pyplot as plt
def cropImage(Image, XY: tuple, WH: tuple, returnGrayscale=False):
    # Extract the x,y and w,h values
    (x, y) = XY
    (w, h) = WH
    # Crop Image with numpy splitting
    crop = Image[y:y + h, x:x + w]
    # Check if returnGrayscale Var is true if is then convert image to grayscale
    if returnGrayscale:
        crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    # Return cropped image
    return crop
image = cv2.imread("C:\\Users\\tqpat\\OneDrive\\Documents\\Python\\Geus\\Model_Data\\serbia_0.jpg")
arr_image = numpy.array(image)
image2 = cropImage(arr_image, (25,36), (174,174))
plt.imshow(image2)
plt.show()