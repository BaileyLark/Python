import mediapipe as mp  
import cv2
import time 

class FaceMeshDetector():
    def __init__(self, staticMode = False, maxFaces=2, redefLandmarks=1, minDetectionCon = 0.5, minTrackCon=0.5):

        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTackCon = minTrackCon


        self.mpDraw = mp.solutions.drawing_utils # function that draws 
        self.mpFaceMesh = mp.solutions.face_mesh 
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=2) # gets the locations
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)


    def findFaceMesh(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converts it to rgb
        self.results = self.faceMesh.process(self.imgRGB) # detects faces, must take rbg
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks: 
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)

                face = []
                for id,lm in enumerate(faceLms.landmark): # x/y/z for each landmark point
                    ih, iw, ic = img.shape # gets pixel values from coords
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    face.append([x, y])
                faces.append(face)
        return img, faces


def main():
    capture = cv2.VideoCapture("video/face1.mp4")
    pTime = 0
    detector = FaceMeshDetector()
    while True: 
        success, img = capture.read() # gets the frame
        img, faces = detector.findFaceMesh(img)
        if len(faces)!= 0:
            print(len(faces[0]))
        cTime = time.time()
        fps = 1 / (cTime- pTime)
        pTime = cTime 
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
        
        cv2.imshow("Image", img) # display the frame 
        cv2.waitKey(1)

if __name__ == "__main__":
    main()


