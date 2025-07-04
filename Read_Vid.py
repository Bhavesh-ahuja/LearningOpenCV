import cv2 as cv 

# Reading Videos

cap = cv.VideoCapture("Videos/Video.mp4")

while True:

  success, frame = cap.read()

  if not success: 
    print("no succ")
    break

  cv.imshow("Video",frame)

  if cv.waitKey(25) & 0xFF == ord('q'):
    break

cap.release()
cv.destroyAllWindows()