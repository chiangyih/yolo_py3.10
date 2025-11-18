import sys

import cv2

#設定視窗名稱及型態
cv2.namedWindow('YOLO', cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('[error] 無法開啟 USB 攝影機，請檢查裝置或裝置編號。')
    sys.exit(1)

try:
    while True:
        ret, frame = cap.read()  #讀取畫面, ret 代表是否成功; frame 代表畫面
        if not ret:
            print('[warn] 無法讀取畫面，可能是裝置中斷或頻寬不足。')
            break

        cv2.imshow('YOLO', frame)
        key = cv2.waitKey(1) & 0xFF  #等待鍵盤輸入, 1 毫秒, 並取得按鍵代碼 ;0xFF 為了相容性,確保只取低位元組
        if key in (27, ord('q')): 
            break
except KeyboardInterrupt:
    print('\n[info] 使用者中斷，正在釋放資源...')
finally:
    cap.release()
    cv2.destroyAllWindows()