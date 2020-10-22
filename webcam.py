import cv2
vid = cv2.VideoCapture(0)

while True:

    sucess,img=vid.read()
    cv2.imshow("shots",img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
