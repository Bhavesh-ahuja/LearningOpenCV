import cv2 as cv
 
#Reading Image 

# Read Image and store in format: NumPy array
img1 = cv.imread('Photos/img1.png')
print(img1)

# Display the image
cv.imshow('Virat Kohli', img1)

# Adds Delay
cv.waitKey(0)

# Closes all the windows 
cv.destroyAllWindows()