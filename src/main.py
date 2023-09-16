from modules.faceMeshModule import detector
import cv2
import pandas as pd
import time
import sys
import os

""" This method is used to detect the face landmarks from a video 
and return a dataframe containing the landmarks"""
def main(path:str):
    # initialize and empty dataframe that will store the ladmarks
    df = None

    cap = cv2.VideoCapture(path)
    
    # Previous Time for frame rate calculations
    pTime = 0

    # Array used to store the face landmarks
    faceArray = []

    # loop while exception is triggered
    while True:
        try:
            success, img = cap.read()
            img , faces = detector.findFaceMesh(img=img)

            if (len(faces)>0):
                faceArray.append(faces)

            # Update current time
            cTime = time.time()

            # Calculate frame rate
            fps = 1 / (cTime - pTime)
            pTime = cTime

            # Display image and landmarks with FPS
            cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                        3, (0, 255, 0), 3)
            cv2.imshow("Image",img)
            cv2.waitKey(1)

            df = pd.DataFrame(faceArray)
        
        except Exception:

            # Will throw an exception once video reaches end , 
            # return the data frame when so
            return df


if __name__ == "__main__":

    # get dataframe from main method
    df = main( os.path.join(sys.path[0],''))

    # save dataframe to excel
    df.to_excel('pandas_to_excel.xlsx', sheet_name='Landmarks')