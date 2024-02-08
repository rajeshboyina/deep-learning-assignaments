import cv2
import time
import os
import handtrackingmodule as hm
def FingersImage(List):
    if sum(List)==0:
        print(0)
        return 0
    elif sum(List)==1:
        print(List.index(1)+1)
        return List.index(1)+1
    elif sum(List)==2:
        if List[0]==1:
            if List==[1,1,0,0,0]:
                print(6)
                return 6
            elif List==[1,0,1,0,0]:
                print(7)
                return 7
            elif List==[1,0,0,1,0]:
                print(8)
                return 8
            elif List==[1,0,0,0,1]:
                print(9)
                return 9
        elif List[1]==1:
            if List==[0,1,1,0,0]:
                print(10)
                return 10
            elif List==[0,1,0,1,0]:
                print(11)
                return 11
            elif List==[0,1,0,0,1]:
                print(12)
                return 12
        elif List[2]==1:
            if List==[0,0,1,1,0]:
                print(13)
                return 13
            elif List==[0,0,1,0,1]:
                print(14)
                return 14
        else:
            print(15)
            return 15
    elif sum(List)==3:
        if List[0]==1:
            if List[1]==1:
                if List==[1,1,1,0,0]:
                    print(16)
                    return 16
                elif List==[1,1,0,1,0]:
                    print(17)
                    return 17
                else:
                    print(18)
                    return 18
            else:
                if List==[1,0,1,0,1]:
                    print(19)
                    return 19
                elif List==[1,0,0,1,1]:
                    print(20)
                    return 20
                else:
                    print(21)
                    return 21
        else:
            if List[1]==1:
                if List==[0,1,1,1,0]:
                    print(22)
                    return 22
                elif List==[0,1,1,0,1]:
                    print(23)
                    return 23
                else:
                    print(24)
                    return 24
            else:
                print(25)
                return 25
    elif sum(List)==4:
        if List[0]==0:
            print(26)
            return 26
        elif List[1]==0:
            print(27)
            return 27
        elif List[2]==0:
            print(28)
            return 28
        elif List[3]==0:
            print(29)
            return 29
        else:
            print(30)
            return 30
    elif sum(List)==5:
        print(-1)
        return -1
key=0
wCam,hCam=1280,720
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
folderPath='fingers_images'
myList=os.listdir(folderPath)
myList=sorted(myList)
print(myList)
overlayList=[]
pTime=0
for imPath in myList:
    image=cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
detector=hm.Handdetector(detectionCon=0.75)
tipsIds=[4,8,12,16,20]
Count=0
while True:
    succuess,img1=cap.read()
    img=cv2.flip(img1,1)
    cv2.rectangle(img, (0, 0), (int(wCam * 0.95), int(hCam * 0.9)-1), (255, 255, 0), int(hCam * 0.21))
    cv2.rectangle(img, ((int(hCam * 0.1)), int(hCam * 0.11)-5), (int(wCam * 0.43), int(hCam * 0.79)), (255, 0, 255), -190)
    cv2.putText(img,'hand geasture moment traking',(130,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.putText(img, 'prepared by Rajesh', (int(0.7*wCam), int(0.95*hCam)), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
    cv2.rectangle(img,((int(hCam * 0.1)),int(hCam * 0.11)),(int(wCam * 0.43), int(hCam * 0.79)),(255,0,255),-190)
    img1=detector.Findhands(img,draw=False)
    imlist=detector.FindPosition(img1,Draw=False)
    # print(imlist)
    if len(imlist)!=0:
        fingers=[]
        #THUMB
        if imlist[tipsIds[0]][1] < imlist[tipsIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #4 FINGERS
        for id in range(1,5):
            if imlist[tipsIds[id]][2]< imlist[tipsIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)
        Count = sum(fingers)
        res = FingersImage(fingers)
        # cv2.rectangle(img,(0,0),(int(wCam*0.95),int(hCam*0.9)),(255,255,0),int(hCam*0.2))
        h,w,c=overlayList[res-1].shape
        # cv2.rectangle(img, (100, 240), (130 + h, 270 + w), (255, 0, 255), 30)
        img[125:h+125,150:w+150]=overlayList[res-1]
        print(res-1)
    else:
        Count=0
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'FPS{int(fps)}',(1150,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),3)
    cv2.putText(img,f'No. of Fingers :{Count}',(130,520),cv2.FONT_HERSHEY_PLAIN,2,(0,220,255),3)
    cv2.imshow("finger counting",img)
    cv2.waitKey(5)
    if key == 27 or cv2.getWindowProperty("finger counting", cv2.WND_PROP_VISIBLE) < 1:
        break

