from modules.faceMeshModule import detector
from main import main
import cv2
import os
import sys


def test_load_video():
    cap = cv2.VideoCapture(os.path.join(sys.path[0], 'test_clips\\JP_500x500.mp4'))
    assert cap.isOpened()


def test_face_detection():
    cap = cv2.VideoCapture(os.path.join(sys.path[0], 'test_clips\\JP_500x500.mp4'))
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img=img)
    assert len(faces) > 0


def test_main():
    assert main(os.path.join(sys.path[0], 'test_clips\\JP_500x500.mp4')) is not None
