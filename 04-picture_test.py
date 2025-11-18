from ultralytics import YOLO
import cv2

target = 'bus.jpg'
model = YOLO('yolov8m.pt')

# print(model.names) #列出模型可辨識的物件名稱

cap = cv2.VideoCapture(target)
if not cap.isOpened():
    print('[error] 無法開啟影像檔案')
    exit(1)

try:
    ret, frame = cap.read()
    if not ret:
        print('[warn] 無法讀取畫面')
    else:
        results = model(frame, verbose=False) #進行物件偵測, verbose=False 不輸出詳細資訊,只回傳結果, results 為包含偵測結果的物件
        frame = results[0].plot() #將偵測結果繪製在影像上, results[0] 代表第一張影像的結果, plot() 方法會回傳繪製後的影像
        cv2.putText(frame, 'YOLOv8m', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL)
        cv2.imshow('YOLOv8', frame)
        while True:
            key = cv2.waitKey(0) & 0xFF
            if key == 27:
                break
except KeyboardInterrupt:
    pass
finally:
    cap.release()
    cv2.destroyAllWindows()

