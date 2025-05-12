# Hand Gesture Video Effect Overlay

Ứng dụng nhận diện số ngón tay bằng Mediapipe và overlay hiệu ứng video tương ứng lên webcam.

## Yêu cầu
- Python 3.8+
- OpenCV (`opencv-python`)
- Mediapipe
- Numpy

## Cài đặt
```bash
pip install -r requirements.txt
```

## Chạy chương trình
Chỉ chạy bằng file sau:
```bash
python main.py
```

## Cấu trúc thư mục
```
main.py
nhan_dien_tay.py
xu_ly_hieu_ung.py
dem_ngon_tay.py
hieu_ung_video.py
README.md
requirements.txt
effects/
    fire.mp4
    lightning.mp4
    rain.mp4
    wind.mp4
    Rasengan.mp4
```

## Lưu ý
- Đặt các file hiệu ứng video vào thư mục `effects/`.
- Khi giơ 1-5 ngón tay, hiệu ứng video tương ứng sẽ xuất hiện trên webcam.

