import cv2

vidcap = cv2.VideoCapture('street_test1.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)#millisec timestamp
    hasFrames,img = vidcap.read()

    #image=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

    if hasFrames:
        cv2.imwrite("C:\\Users\\my3kr\\PycharmProjects\\vehicle_detect\\vehicledetect\\samplesholder\\frame%d.jpg" % count, img)

        return hasFrames
sec = 0
frameRate = 1
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)