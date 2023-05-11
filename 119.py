import cv2
import math
video=cv2.VideoCapture("119/footvolleyball.mp4")



returned,myimage=video.read()

Tracker=cv2.TrackerCSRT_create()
print(Tracker)

bbox=cv2.selectROI("tracking",myimage,False)
print("what is bbox: ",bbox)

Tracker.init(myimage,bbox)

p1=520
p2=300

new_x=[]
new_y=[]
def draw_box(image,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]), int(bbox[3])
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(image,"Tracking",(300,200),cv2.FONT_HERSHEY_COMPLEX,0.7,(9,0,255),2)

def goal_tracker(image,bbox):
    cv2.circle(image,(p1,p2),3,(0,255,0),3)
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]), int(bbox[3])
    c1=x+int(w/2)
    c2=y+int(h/2)

    cv2.circle(image,(c1,c2),2 ,(0,0,255),5 )

    distance=math.sqrt(((c1-p1)**2)+((c2-p2)**2))
    print("what is D: ",distance)

    new_x.append(c1)
    new_y.append(c2)

    for i in range(len(new_x)):
        cv2.circle(image,(new_x[i],new_y[i]),3,(255,0,255),3)

    if(distance<=15 ):
             cv2.putText(frame,"Well done my guy/girl",(200,400),cv2.FONT_HERSHEY_COMPLEX,0.7,(9,0,255),2)

while True:
    dummy, frame=video.read()
    success,mybox=Tracker.update(frame)


    if success==True:
        draw_box(frame,mybox)
    else:
        cv2.putText(frame,"lost",(300,200),cv2.FONT_HERSHEY_COMPLEX,0.7,(9,0,255),2)


    goal_tracker(frame,mybox  )

    cv2.imshow("basketballllll", frame)

    if cv2.waitKey(1)==29:
 
        break
video.release()
cv2.destroyAllWindows()