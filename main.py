from sensors.door_sensor import OutdoorSensor
from sensors import OutdoorSensorSub
from cctv.camera import create_camera, camera_make_shot

from threading import Thread, Lock
import time

import cv2

# outdoor_sensor = OutdoorSensor()
# bot_subscriber = OutdoorSensorSub()

# outdoor_sensor.subscribers_manager.subscribe(bot_subscriber)


# sensor_thread = Thread(target=outdoor_sensor.listen_sensor)
# sensor_thread.start()


cam = create_camera()

# while True:

inp = input("type something ")

if inp == '1':
    for i in range(2):
        # success, current_cam = cam.read()
        # dim = (width, height)

        # resized_frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_LINEAR)
        # # print(type(current_cam))
        resized_frame = camera_make_shot(cam)
        
        cv2.imshow('screen', resized_frame)
        cv2.waitKey(0)
        
        time.sleep(1)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     break