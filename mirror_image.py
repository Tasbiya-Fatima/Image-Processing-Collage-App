import cv2

# Read image
img = cv2.imread("C:\Internship\Assignment\ASS4\download.jpg")

# Get height, width, channels
h, w, c = img.shape

# Create empty image
mirror = img.copy()

# Mirror logic
for y in range(h):
    for x in range(w):
        mirror[y, x] = img[y, w - x - 1]

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Mirror Image", mirror)

cv2.waitKey(0)
cv2.destroyAllWindows()
