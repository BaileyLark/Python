import cv2 
import mediapipe as mp 
import time

class poseDetector():
    def __init__(self, mode=False, upBody=False, model_complexity=1, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode 
        self.upBody = upBody
        self.model_complexity = model_complexity
        self.smooth = smooth 
        self.detectionCon = detectionCon
        self.trackCon = trackCon 
        
        self.mpPose = mp.solutions.pose 
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.model_complexity, self.smooth, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self, img, draw=True):

        imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converts the video
        results = self.pose.process(imgRBG) # adds landmarks 
        if results.pose_landmarks: # if pose is detected
            if draw: 
                self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
       
        return img

        ''' 
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape 
                cx, cy = int(lm.x*w), int(lm.y*h) 
                
        results.pose_landmarks
        '''


def main():
    pTime = 0 
    cap = cv2.VideoCapture('video\dance1.mp4')
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
        cv2.imshow("img", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
