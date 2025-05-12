import cv2
import numpy as np

def overlay_image(background, overlay, x, y):
    h, w = overlay.shape[:2]
    bh, bw = background.shape[:2]
    x1, y1 = max(x, 0), max(y, 0)
    x2, y2 = min(x + w, bw), min(y + h, bh)
    overlay_x1, overlay_y1 = x1 - x, y1 - y
    overlay_x2, overlay_y2 = overlay_x1 + (x2 - x1), overlay_y1 + (y2 - y1)
    if x1 >= x2 or y1 >= y2:
        return
    roi = background[y1:y2, x1:x2]
    overlay_roi = overlay[overlay_y1:overlay_y2, overlay_x1:overlay_x2]
    alpha = overlay_roi[:, :, 3:4] / 255.0
    background[y1:y2, x1:x2] = (1 - alpha) * roi + alpha * overlay_roi[:, :, :3]
    background[y1:y2, x1:x2] = background[y1:y2, x1:x2].astype(np.uint8)

class VideoEffect:
    def __init__(self, path, size=(500, 500)):
        self.cap = cv2.VideoCapture(path)
        self.size = size
        self.frame = None
        self.valid = self.cap.isOpened()
    def get_frame(self):
        if not self.valid:
            return None
        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()
            if not ret:
                return None
        frame = cv2.resize(frame, self.size)
        return frame
    def release(self):
        if self.cap:
            self.cap.release()
