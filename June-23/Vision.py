import cv2 
import mediapipe as mp 
import time 

capture = cv2.VideoCapture(0)

# gets the api and allows use 
mpHands = mp.solutions.hands 
hands = mpHands.Hands() # an object that calls hands() looks for 2 hands, without static image
mpDraw = mp.solutions.drawing_utils # function that draws landmarks

pTime = 0 
cTime = 0 

while True:
    success, img = capture.read() # reads the frames
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # video takes in BGR, so convert
    results = hands.process(imgRBG) # calls the function 

    if results.multi_hand_landmarks: 
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape #gets size of screen
                cx, cy = int(lm.x*w), int(lm.y*h) # converts values to pixel dimensions 
                if id==0:
                    cv2.circle(img, (cx, cy), 40, (255, 255, 255, cv2.FILLED))

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # FPS    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime 
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255,255,255), 3)


    cv2.imshow("Image", img) # displays the frames
    cv2.waitKey(1) # waits for user input to close


