import cv2

img = cv2.imread(r"C:\Internship\Assignment\ASS4\1.png")
img2 = img.copy()

h, w, c = img.shape

for y in range(h):
    for x in range(w):
        b, g, r = img[y][x]
        img2[y][x] = (0, g, 0)

# Create resizable windows
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Greenscale Image", cv2.WINDOW_NORMAL)

# Set window size
cv2.resizeWindow("Original Image", 500, 400)
cv2.resizeWindow("Greenscale Image", 500, 400)

cv2.imshow("Original Image", img)
cv2.imshow("Greenscale Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
