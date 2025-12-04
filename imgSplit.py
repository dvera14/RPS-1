import cv2 as cv
import sys

# Open the default camera
cam = cv.VideoCapture(0)

# Get the default frame width and height
frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))



 
last_frame = None

print("Press 'q' to take snapshot.")

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv.imshow('Camera', frame)

    last_frame = frame

    # Press 'q' to exit the loop
    if cv.waitKey(1) == ord('q'):
        break

if last_frame is not None:
    cv.imwrite('last_frame.jpg', last_frame)
    print("Snapshot saved as 'last_frame.jpg'")

# Release the capture and writer objects

cam.release()
out.release()
cv.destroyAllWindows()

img = cv.imread('last_frame.jpg')

if img is None:
    print("Could not read the image.")
    sys.exit()


#Splitting the image in 4

h,w, channels = img.shape

half_width = w // 2
half_height = h // 2

# Splitting into 4 parts. These are numpy 2d arrays
top_left = img[:half_height, :half_width]
top_right = img[:half_height, half_width:]
bottom_left = img[half_height:, :half_width]
bottom_right = img[half_height:, half_width:]

print("Saved: top_left.jpg, top_right.jpg, bottom_left.jpg, bottom_right.jpg")






# saving all the images
# cv2.imwrite() function will save the image 
# into your pc
cv.imwrite('top_left.jpg', top_left)
cv.imwrite('top_right.jpg', top_right)
cv.imwrite('bottom_left.jpg', bottom_left)
cv.imwrite('bottom_right.jpg', bottom_right)
cv.waitKey(0)



