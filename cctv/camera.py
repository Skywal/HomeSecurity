import cv2
import numpy as np

from options import RTSP


class Camera:
    
    DEFAULT_WIDTH: int = 1600
    DEFAULT_HEIGHT: int = 900

    def __init__(self) -> None:
        self.camera: cv2.VideoCapture = cv2.VideoCapture()
        self.rtsp: str = f"rtsp://{RTSP.USERNAME}:{RTSP.PASSWORD}@{RTSP.ADDRESS}/stream1"

        
    def set_rtsp(self, rtsp_str: str) -> None:
        if rtsp_str:
            self.rtsp = rtsp_str


    def make_single_shot(self, is_resize: bool = True, width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT) -> bytes:
        """
        Open video stream defined in 'rtsp' attribute. Make photo and close stream.
        """
        
        self.camera.open(self.rtsp)

        if not self.camera.isOpened():
            self.camera.release()
            return self._make_image_bytes(np.zeros((100, 100)))
        
        success, image = self.camera.read()
        self.camera.release()

        if success:
    
            resized_frame = image

            if is_resize:
                dim = (width, height)
                resized_frame = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
        
            return self._make_image_bytes(resized_frame)
    
        return self._make_image_bytes(np.zeros((100, 100)))


    def _make_image_bytes(self, cv2_image: np.ndarray) -> bytes:
        is_success, im_buf_arr = cv2.imencode(".jpeg", cv2_image)
        byte_image = im_buf_arr.tobytes()

        return byte_image
    
    
if __name__ == "__main__":
    pass
