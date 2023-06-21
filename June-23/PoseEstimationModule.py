import cv2 
import mediapipe as mp 
import time


mpPose = mp.solutions.pose 
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture('video\dance1.mp4')
pTime = 0 
while True:
    success, img = cap.read()
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRBG)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    results.pose_landmarks
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)

    cv2.imshow("img", img)
    cv2.waitKey(1)
