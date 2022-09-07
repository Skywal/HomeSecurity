import cv2
import numpy as np

from options import RTSP

WIDTH = 1920
HEIGHT = 1080

# TODO: Make check if VideoCapture stream has opened
def create_camera() -> cv2.VideoCapture:
    rtsp = f"rtsp://{RTSP.USERNAME}:{RTSP.PASSWORD}@{RTSP.ADDRESS}/stream1"
    cap = cv2.VideoCapture()
    cap.open(rtsp)
    
    return cap

def camera_make_shot(camera: cv2.VideoCapture, is_resize: bool = True, width: int = WIDTH, height: int = HEIGHT) -> np.ndarray:
    success, current_cam = camera.read()
    if success:
    
        resized_frame = current_cam

        if is_resize:
            dim = (width, height)
            resized_frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_LINEAR)
        
        return resized_frame
    
    return np.zeros((100, 100))


if __name__ == "__main__":
    pass
