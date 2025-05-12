import os
from xu_ly_hieu_ung import VideoEffect

def tai_hieu_ung_video():
    video_effect_files = {
        1: 'fire.mp4',
        2: 'lightning.mp4',
        3: 'rain.mp4',
        4: 'wind.mp4',
        5: 'Rasengan.mp4',
    }
    video_effects = {}
    for k, filename in video_effect_files.items():
        path = os.path.join('effects', filename)
        video_effects[k] = VideoEffect(path)
    return video_effects
