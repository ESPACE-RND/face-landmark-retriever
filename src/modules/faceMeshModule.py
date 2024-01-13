import cv2
import mediapipe as mp

""" This class is used to detect the face landmarks from a video"""


class FaceMeshDetector():
    """ This method is used to initialize the class"""

    def __init__(self, staticMode=False, maxFaces=2, minDetection=0.5,
                 minTrackCon=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetection = minDetection
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh()
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    """ This method is used to detect the face landmarks from 
    a video and return the image and the landmarks"""

    def findFaceMesh(self, img, draw=True):

        try:
            # Convert to RGB
            self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.results = self.faceMesh.process(self.imgRGB)
            faces = []

            # Check if faces are detected
            if self.results.multi_face_landmarks:
                for faceLms in self.results.multi_face_landmarks:
                    # Draw the landmarks
                    if draw:
                        self.mpDraw.draw_landmarks(img, faceLms,
                                                   self.mpFaceMesh.FACEMESH_CONTOURS,
                                                   self.drawSpec, self.drawSpec)
                    face = []
                    # Loop through the landmarks and append to array
                    for id, lm in enumerate(faceLms.landmark):
                        face.append([lm.x, lm.y, lm.z])
                    faces.append(face)
            return img, faces
        except Exception:
            pass


# Create an instance of the class
detector = FaceMeshDetector()
