import cv2

# Read image
img = cv2.imread(r"C:\Internship\Assignment\ASS4\1.png")  # use raw string
img2 = img.copy()

h, w, c = img.shape

threshold = 128  # Set threshold for binary

for y in range(h):
    for x in range(w):
        b, g, r = img[y][x]
        avg = int((int(b) + int(g) + int(r)) / 3)  # grayscale value
        if avg > threshold:
            img2[y][x] = (255, 255, 255)  # white
        else:
            img2[y][x] = (0, 0, 0)        # black

cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
