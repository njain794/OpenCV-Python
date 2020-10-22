import cv2

framewidth=480
frameheight=100

vid = cv2.VideoCapture("resources/shots.mp4")

while True:

    sucess,img=vid.read()
    img=cv2.resize(img,(framewidth,frameheight))
    cv2.imshow("shots",img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
