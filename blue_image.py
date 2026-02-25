import cv2

img = cv2.imread(r"C:\Internship\Assignment\ASS4\1.png")
img2 = img.copy()

h, w, c = img.shape

for y in range(h):
    for x in range(w):
        b, g, r = img[y][x]
        avg = int((int(b) + int(g) + int(r)) / 3)
        img2[y][x] = (b, 0, 0)

cv2.imshow("Original Image", img)
cv2.imshow("bluescale Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()