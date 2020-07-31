from cv2 import cv2
import numpy as np
import math
import serial

from utils import trackbar
from utils import image_utils

# ************ VARIABLES ************
PORT = "/dev/cu.usbmodem141101"
VIDEO_WIDTH = 640
VIDEO_HEIGHT = 480
VIDEO_BRIGHTNESS = 230
CROP_VALUES = 720, 0, 440, 600

# ************ WINDOWS ************
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 960, 640)

tb = trackbar.TrackBar()

# connect to serial monitor
try:
    ser = serial.Serial(PORT, 115200)
except:
    print("Could not connect to serial monitor")

# start video camera
cap = cv2.VideoCapture(0)
cap.set(3, VIDEO_WIDTH)
cap.set(4, VIDEO_HEIGHT)
cap.set(10, VIDEO_BRIGHTNESS)

while True:
    # read frame from video
    _, img = cap.read()

    # apply blur and hsv filters to image
    img_blur = cv2.GaussianBlur(img, (7, 7), 1)
    img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

    # get trackbar values
    h_min, h_max, s_min, s_max, v_min, v_max = tb.getTrackBarPos()
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # use trackbar vlaues to create a mask
    img_mask = cv2.inRange(img_hsv, lower, upper)
    img_result = cv2.bitwise_and(img, img, mask=img_mask)

    # crop image to isolate hand
    img_cropped = img_mask[CROP_VALUES[1]:CROP_VALUES[2] +
                           CROP_VALUES[1], CROP_VALUES[0]:CROP_VALUES[0]+CROP_VALUES[3]]
    img_result = img_result[CROP_VALUES[1]:CROP_VALUES[2] +
                            CROP_VALUES[1], CROP_VALUES[0]: CROP_VALUES[0] + CROP_VALUES[3]]

    # apply dilation and erosion filters to smoothen image
    img_open = cv2.morphologyEx(
        img_cropped, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    img_closed = cv2.morphologyEx(
        img_open, cv2.MORPH_CLOSE, np.ones((10, 10), np.uint8))

    # apply bilateral filter to closed image
    img_filter = cv2.bilateralFilter(img_closed, 5, 75, 75)

    # use image function to outline hand object and count the fingers
    img_contour, img_result, finger_count = image_utils.getContours(
        img_filter, img_result)

    # send finger count data to serial monitor
    try:
        number = f"{finger_count}"
        ser.write(number.encode())
    except:
        pass

    # draw rectangle aroud cropped area in original image
    cv2.rectangle(img, (CROP_VALUES[0], CROP_VALUES[1]), (CROP_VALUES[0] +
                                                          CROP_VALUES[3], CROP_VALUES[2] + CROP_VALUES[1]), (0, 255, 0), 2)

    # stack photos together to output
    stackedImage = image_utils.stackImages(0.7, ([img, img_mask, img_filter], [
        img_cropped, img_contour, img_result]))

    # show stacked image
    cv2.imshow('Video', stackedImage)

    # wait for keypress to quit
    if cv2.waitKey(1) and 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
