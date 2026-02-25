import cv2

img = cv2.imread(r"C:\Internship\Assignment\ASS4\download.jpg")
img2 = img.copy()

h, w, c = img.shape

for y in range(h):
    for x in range(w):
        b, g, r = img[y][x]
        avg = int((int(b) + int(g) + int(r)) / 3)
        img2[y][x] = (avg, avg, avg)

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()