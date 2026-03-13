import cv2 as cv
import sys

# Read an image from the specified file path
img = cv.imread(cv.samples.findFile("hetal.png"))

# Check if the image was loaded successfully
if img is None:
    sys.exit("Could not read the image.")

# Display the image in a window named "Display window"
cv.imshow("Display window", img)

# Wait for a keystroke in the window (0 means wait indefinitely)
k = cv.waitKey(0)

# If the 's' key is pressed, save the image
if k == ord("s"):
    cv.imwrite("hetal.png", img)
