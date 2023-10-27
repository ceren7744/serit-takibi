import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = 'yol1.jpg'
img = cv2.imread(img_path)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
canny_image = cv2.Canny(binary_image, 180, 255)
lines = cv2.HoughLinesP(canny_image, 1, np.pi/180, threshold=30)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
def mask_of_image(image):
    height = image.shape[0]
    polygons = np.array([[(0, height), (2200, height), (250, 100)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image
roi_image = mask_of_image(img)
plt.subplot(131), plt.imshow(img), plt.title('Orjinal Görüntü')
plt.subplot(132), plt.imshow(canny_image, cmap='gray'), plt.title('Kenarlar')
plt.subplot(133), plt.imshow(roi_image), plt.title('ROI ve Algılanan Çizgiler')

plt.show()



