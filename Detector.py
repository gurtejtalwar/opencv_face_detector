from cv2 import cv2

# Loads pre-trained data from opencv (haar cascade algorithm)
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Captures video from webcam
webcam=cv2.VideoCapture(0)
key=cv2.waitKey(1)

# Iterates over frames forever
while True:
    ### Reads the current frame
    successful_frame_read, frame=webcam.read()
    
    # Convert to grayscale
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # Detects Faces(Coordinates)
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    print(face_coordinates)                              
   
    # Draw rectangle around the face
    for(x,y,w,h) in face_coordinates:   
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow('Face Detector',frame)
    cv2.waitKey(1)
    
           

    """
# Detects Faces
face_coordinates=trained_face_data.detectMultiScale(grayscaled_frame)
#print(face_coordinates)

# Draw rectangle around the face
for(x,y,w,h) in face_coordinates:
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)


#
cv2.imshow('Robert Downey',frame)
cv2.waitKey()
    """
print("code completed")     