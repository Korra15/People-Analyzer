import cv2
 

def main():
    name=input("Enter your name")
    windowname = "Writing A Video"
    cv2.namedWindow(windowname)
 
 
    cap = cv2.VideoCapture(0)
 
    filepath="D:\\mini project\\mini\\People-Analyzer\\OpenCV\\User_Videos\\"

    filename = (filepath+name+".avi")
    codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    framerate = 29
    resolution = (640, 480)
 
 
    VideoOutPut = cv2.VideoWriter(filename, codec, framerate, resolution)
 
 
    if cap.isOpened():
        ret, frame = cap.read()
 
    else:
        ret = False
 
 
    while ret:
        ret, frame = cap.read()
 
 
        VideoOutPut.write(frame)
        if  cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
    cv2.destroyAllWindows()
    VideoOutPut.release()
    cap.release()
 
 
if __name__ == "__main__":
    main()