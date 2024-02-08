import cv2
import mediapipe as mp
import time
key=-1
class Handdetector():
    def __init__(self,mode=False,maxHands=2,modelComp=1, detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.modelComp=modelComp
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode, self.maxHands, self.modelComp, self.detectionCon)
        self.mpDraw=mp.solutions.drawing_utils

    def Findhands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    def FindPosition(self, img, HandNo=0, Draw=True):
        lmlist=[]
        if self.results.multi_hand_landmarks:
            MyHand=self.results.multi_hand_landmarks[HandNo]
            for id, lm in enumerate(MyHand.landmark):
                h, w, c=img.shape
                cx, cy= int(lm.x*w),int(lm.y*h)
                lmlist.append([id, cx, cy])
                if Draw:
                    cv2.circle(img,(cx,cy),7,(255,0,0),cv2.FILLED)
        return lmlist
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector=Handdetector()
    while True:
        success, img = cap.read()
        img=detector.Findhands(img)
        lmlist=detector.FindPosition(img)
        if len(lmlist)!=0:
            print(lmlist[4])
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
        if key == 27 or cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
            break





if __name__=="__main__":
    main()