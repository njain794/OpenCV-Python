import cv2

framewidth=640
frameheight=360
vid = cv2.VideoCapture(0)
vid.set(3,framewidth)
vid.set(4,frameheight)

while True:

    sucess,img=vid.read()
    cv2.imshow("shots",img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
