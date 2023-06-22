import cv2 
import mediapipe as mp 
import time 

class handDetector():
    def __init__(self, mode=False, maxHands=2, model_complexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode 
        self.maxHands = maxHands 
        self.detectionCon = detectionCon
        self.model_complexity = model_complexity

        self.trackCon = trackCon 
    
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity, self.detectionCon, self.trackCon) # an object that calls hands() looks for 2 hands, without static image
        self.mpDraw = mp.solutions.drawing_utils # function that draws landmarks
    
    def findHands(self, img, draw=True):
        imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # video takes in BGR, so convert
        self.results = self.hands.process(imgRBG) # calls the function 

        if self.results.multi_hand_landmarks: 
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img  

    def findposition(self, img, handNo=0, draw=True, coord=False):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo] # gets landmark array of first hand
            for id, lm in enumerate(myHand.landmark): # goes through the landmark coords
                h, w, c = img.shape #gets size of screen
                cx, cy = int(lm.x*w), int(lm.y*h) # converts values to pixel dimensions 
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        if len(lmList) != 0 and coord:
            cv2.putText(img, "x:" + (str(lmList[handNo][1]) + " y:" + str(lmList[handNo][2])), (lmList[handNo][1], lmList[handNo][2]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
        return lmList


def main():

    pTime = 0 
    cTime = 0 
    capture = cv2.VideoCapture(0)
    
    detector = handDetector()

    while True:
        success, img = capture.read() # reads the frames
        img = detector.findHands(img)
        lmList = detector.findposition(img)
        if len(lmList) != 0:
            print(lmList[0][1])

        # FPS    
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime 

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255,255,255), 3)

        cv2.imshow("Image", img) # displays the frames
        cv2.waitKey(1) # waits for user input to close

if __name__ == "__main__":
    main()
