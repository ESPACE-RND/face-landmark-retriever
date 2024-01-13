from modules.faceMeshModule import detector
from modules.datasetCreationModule import  split_video_and_extract_audio
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

    # Specify the input folder containing videos
    input_folder = "C:/Users/Admin/PycharmProjects/faceDet/src/Training/clips"

    # Specify the output folder for saving video segments
    video_output_folder = "C:/Users/Admin/PycharmProjects/faceDet/src/Training/extracted_clips"

    # Specify the output folder for saving audio segments
    audio_output_folder = "C:/Users/Admin/PycharmProjects/faceDet/src/Training/extracted_audio"

    # # Iterate through each video file in the input folder
    # for filename in os.listdir(input_folder):
    #     if filename.endswith(".mp4"):
    #         video_path = os.path.join(input_folder, filename)
    #         split_video_and_extract_audio(video_path, video_output_folder, audio_output_folder)

    # Iterate through each video file in the input folder
    for filename in os.listdir(video_output_folder):
        if filename.endswith(".mp4"):
            # get dataframe from main method
            df = main(os.path.join(video_output_folder, filename))

            # save dataframe to excel
            df.to_excel(f"C:/Users/Admin/PycharmProjects/faceDet/src/Training/excel_files/{filename}_pandas_to_excel.xlsx", sheet_name='Landmarks')
