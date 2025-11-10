"""import cv2
vid = cv2.VideoCapture(0)
while(True):
      

    Red = 0
    Green = 0
    Blue = 0

    
    ret, frame = vid.read(0)
    cv2.imshow("Camera",frame)
    rgb_values = frame.reshape(-1, 3)  # Reshape frame to a 2D array of pixels
    for pixel in rgb_values:
        r, g, b = pixel
        Red += r
        Green += g
        Blue += b
        
    if (Red + Green + Blue )/3< 7799766:
        print("Tampered")

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
  


vid.release()
cv2.destroyAllWindows()"""