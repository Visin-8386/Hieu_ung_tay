import math

def dem_ngon_tay(lm):
    finger_joints = [(4, 3), (8, 6), (12, 10), (16, 14), (20, 18)]
    count = 0
    raised_finger_tip = None
    thumb_tip = lm[4]
    thumb_ip = lm[3]
    wrist = lm[0]
    if thumb_tip.x < thumb_ip.x and thumb_tip.x < wrist.x:
        count += 1
        if count == 1:
            raised_finger_tip = thumb_tip
    for idx, (tip_id, pip_id) in enumerate(finger_joints[1:], start=1):
        tip = lm[tip_id]
        pip = lm[pip_id]
        if tip.y < pip.y:
            count += 1
            if count == 1:
                raised_finger_tip = tip
    return count, raised_finger_tip
