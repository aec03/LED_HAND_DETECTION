from cv2 import cv2


class TrackBar():
    def __init__(self):
        cv2.namedWindow("trackBars")

        cv2.resizeWindow("trackBars", 640, 240)

        def empty(a): pass

        cv2.createTrackbar("Hue min", "trackBars", 0, 179, empty)
        cv2.createTrackbar("Hue max", "trackBars", 179, 179, empty)
        cv2.createTrackbar("Sat min", "trackBars", 50, 255, empty)
        cv2.createTrackbar("Sat max", "trackBars", 255, 255, empty)
        cv2.createTrackbar("Value min", "trackBars", 0, 255, empty)
        cv2.createTrackbar("Value max", "trackBars", 255, 255, empty)

    def getTrackBarPos(self):
        h_min = cv2.getTrackbarPos("Hue min", "trackBars")
        h_max = cv2.getTrackbarPos("Hue max", "trackBars")
        s_min = cv2.getTrackbarPos("Sat min", "trackBars")
        s_max = cv2.getTrackbarPos("Sat max", "trackBars")
        v_min = cv2.getTrackbarPos("Value min", "trackBars")
        v_max = cv2.getTrackbarPos("Value max", "trackBars")

        return h_min, h_max, s_min, s_max, v_min, v_max
