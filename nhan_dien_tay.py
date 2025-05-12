import cv2
import mediapipe as mp
import numpy as np
from xu_ly_hieu_ung import overlay_image
from xu_ly_hieu_ung import VideoEffect
from dem_ngon_tay import dem_ngon_tay
from hieu_ung_video import tai_hieu_ung_video

def main():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    video_effects = tai_hieu_ung_video()
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            h, w = frame.shape[:2]
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)
            show_effect = None
            effect_pos = (0, 0)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    lm = hand_landmarks.landmark
                    cx, cy = int(lm[0].x * w), int(lm[0].y * h)
                    count, raised_finger_tip = dem_ngon_tay(lm)
                    if count in video_effects and video_effects[count].valid:
                        if count == 1 and raised_finger_tip is not None:
                            effect_pos = (int(raised_finger_tip.x * w), int(raised_finger_tip.y * h) - 60)
                        elif count == 5:
                            palm_x = int(sum([lm[i].x for i in [0, 1, 5, 9, 13, 17]]) / 6 * w)
                            palm_y = int(sum([lm[i].y for i in [0, 1, 5, 9, 13, 17]]) / 6 * h)
                            effect_pos = (palm_x, palm_y)
                        else:
                            effect_pos = (cx, cy)
                        show_effect = count
            if show_effect in video_effects:
                effect_video = video_effects[show_effect]
                effect_frame = effect_video.get_frame()
                if effect_frame is not None:
                    if effect_frame.shape[2] == 3:
                        effect_frame = cv2.cvtColor(effect_frame, cv2.COLOR_BGR2BGRA)
                    if show_effect == 5:
                        lower_black = np.array([0, 0, 0])
                        upper_black = np.array([50, 50, 50])
                        mask = cv2.inRange(effect_frame[:, :, :3], lower_black, upper_black)
                        alpha = 255 - mask
                        effect_frame[:, :, 3] = alpha
                    else:
                        hsv = cv2.cvtColor(effect_frame[:, :, :3], cv2.COLOR_BGR2HSV)
                        lower_green = np.array([35, 40, 40])
                        upper_green = np.array([85, 255, 255])
                        mask = cv2.inRange(hsv, lower_green, upper_green)
                        alpha = 255 - mask
                        effect_frame[:, :, 3] = alpha
                    x = effect_pos[0] - effect_frame.shape[1] // 2
                    y = effect_pos[1] - effect_frame.shape[0] // 2
                    overlay_image(frame, effect_frame, x, y)
            cv2.imshow('Hand Detection', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()
    for v in video_effects.values():
        v.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
