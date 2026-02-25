import cv2
import numpy as np

# Read Image (Change path if needed)
img = cv2.imread("1.png")

if img is None:
    print("Image not found!")
    exit()

h, w, c = img.shape

# Create copies
gray = img.copy()
binary = img.copy()
red = img.copy()
green = img.copy()
blue = img.copy()
mirror = img.copy()

threshold = 128

# Apply effects
for y in range(h):
    for x in range(w):
        b, g, r = img[y][x]
        avg = int((int(b) + int(g) + int(r)) / 3)

        # Gray
        gray[y][x] = (avg, avg, avg)

        # Binary
        if avg > threshold:
            binary[y][x] = (255, 255, 255)
        else:
            binary[y][x] = (0, 0, 0)

        # Red
        red[y][x] = (0, 0, r)

        # Green
        green[y][x] = (0, g, 0)

        # Blue
        blue[y][x] = (b, 0, 0)

        # Mirror
        mirror[y, x] = img[y, w - x - 1]

# Resize all images to same size (optional)
size = (400, 300)

img_r = cv2.resize(img, size)
gray_r = cv2.resize(gray, size)
binary_r = cv2.resize(binary, size)
red_r = cv2.resize(red, size)
green_r = cv2.resize(green, size)
blue_r = cv2.resize(blue, size)
mirror_r = cv2.resize(mirror, size)

# Create collage (2 rows x 4 columns)
row1 = np.hstack((img_r, gray_r, binary_r, mirror_r))
row2 = np.hstack((red_r, green_r, blue_r, img_r))

collage = np.vstack((row1, row2))

# Show collage
cv2.namedWindow("Image Collage", cv2.WINDOW_NORMAL)
cv2.imshow("Image Collage", collage)

cv2.waitKey(0)
cv2.destroyAllWindows()