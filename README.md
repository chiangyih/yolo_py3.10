# YOLOv8 專案

作者：Tseng chiang yih

使用 Ultralytics YOLOv8 進行物件偵測，包含 GPU 環境檢查、YOLO 設定查看、USB 攝影機即時畫面顯示、靜態影像推論與人類（person）偵測示範。

測試環境：Windows 11 25H2、Python 3.10.19、PyTorch 2.9.1 + CUDA 13.0

## 內容導覽

- 快速開始
- 專案腳本一覽
- 環境需求
- 模型與測試素材
- YOLOv8 模型名稱（Detection / Segmentation / Pose / Classification）
- YOLO 可偵測類別清單（COCO 80 類）
- 常見問題

## 快速開始

```pwsh
python 01-gpu_cuda_test.py
python 04-picture_test.py
python 03-usb_webcam_test.py
python 06-human_detect.py
python 07-person_count.py
```

## 專案腳本一覽

| 檔案 | 用途 | 來源 | 操作 |
|---|---|---|---|
| `01-gpu_cuda_test.py` | 驗證 GPU/CUDA | 無 | 直接執行 | 
| `02-檢查當前yolo配置.py` | 查看 Ultralytics 設定 | 無 | 直接執行 | 
| `03-usb_webcam_test.py` | USB 攝影機即時顯示 | USB webcam | `ESC` 或 `q` 退出（視窗需取得焦點） |
| `04-picture_test.py` | 靜態影像偵測 | `bus.jpg` | `ESC` 退出 |
| `05-video_test.py` | 串流/影片偵測展示 | RTSP/HTTP/MP4 | `ESC` 退出（需自行修改 `target`） |
| `06-human_detect.py` | 人類（person）即時偵測 | USB webcam | `ESC` 退出 |
| `07-person_count.py` | 人數計算（person 計數）即時偵測 | USB webcam | `ESC` 退出 |

<details>
<summary>展開：各腳本詳細說明</summary>

### `01-gpu_cuda_test.py`
- 檢查 PyTorch 版本、CUDA 是否可用、GPU 數量、cuDNN 狀態與顯示卡記憶體狀態。

### `02-檢查當前yolo配置.py`
- 列印 Ultralytics `settings`，並讀取 `runs_dir`（目前程式只取值未額外列印）。

### `03-usb_webcam_test.py`
- 開啟 USB 攝影機（預設編號 0）並即時顯示。
- 視窗可調整大小（`cv2.WINDOW_NORMAL`）。

### `04-picture_test.py`
- 讀取 `bus.jpg` 後進行偵測，左上角顯示 `YOLOv8m`，按 `ESC` 關閉視窗。

### `06-human_detect.py`
- 使用 `yolov8m.pt` 對 USB 攝影機即時推論，只偵測 person 並框選，影像大小固定 640×480。

### `07-person_count.py`
- 基於 `06-human_detect.py`，額外計算畫面中的 person 數量，並在視窗右上角以粗體顯示。

### `05-video_test.py`
- 從 RTSP/HTTP/MP4 讀取畫面並進行偵測，畫面顯示 FPS。
- 請先修改 `target` 來源再執行；目前程式結束時未顯式 `release/destroyAllWindows`。

</details>

## 環境需求

- Python 3.8+
- PyTorch
- OpenCV（`opencv-python`）
- Ultralytics YOLOv8（`ultralytics`）
- NVIDIA GPU（建議但非必需）

## 模型與測試素材

- `yolov8m.pt`：YOLOv8 中等模型（Medium）
- `bus.jpg`：示範影像

## YOLOv8 模型名稱

以下列出 YOLOv8 常見的模型大小（n/s/m/l/x）與權重檔名。不同任務會有不同後綴：
- 偵測：無後綴（例如 `yolov8m.pt`）
- 分割：`-seg`
- 姿態：`-pose`
- 分類：`-cls`

<details>
<summary>展開：偵測 Detection（無後綴）</summary>

| 模型代號 | 權重檔名 | 說明 |
|---|---|---|
| YOLOv8n | `yolov8n.pt` | Nano：速度最快、精度較低 |
| YOLOv8s | `yolov8s.pt` | Small：速度/精度平衡（偏快） |
| YOLOv8m | `yolov8m.pt` | Medium：速度/精度平衡 |
| YOLOv8l | `yolov8l.pt` | Large：精度較高、速度較慢 |
| YOLOv8x | `yolov8x.pt` | XLarge：精度最高、速度最慢 |

</details>

<details>
<summary>展開：分割 Segmentation（`-seg`）</summary>

| 模型代號 | 權重檔名 |
|---|---|
| YOLOv8n-seg | `yolov8n-seg.pt` |
| YOLOv8s-seg | `yolov8s-seg.pt` |
| YOLOv8m-seg | `yolov8m-seg.pt` |
| YOLOv8l-seg | `yolov8l-seg.pt` |
| YOLOv8x-seg | `yolov8x-seg.pt` |

</details>

<details>
<summary>展開：姿態 Pose（`-pose`）</summary>

| 模型代號 | 權重檔名 |
|---|---|
| YOLOv8n-pose | `yolov8n-pose.pt` |
| YOLOv8s-pose | `yolov8s-pose.pt` |
| YOLOv8m-pose | `yolov8m-pose.pt` |
| YOLOv8l-pose | `yolov8l-pose.pt` |
| YOLOv8x-pose | `yolov8x-pose.pt` |

</details>

<details>
<summary>展開：分類 Classification（`-cls`）</summary>

| 模型代號 | 權重檔名 |
|---|---|
| YOLOv8n-cls | `yolov8n-cls.pt` |
| YOLOv8s-cls | `yolov8s-cls.pt` |
| YOLOv8m-cls | `yolov8m-cls.pt` |
| YOLOv8l-cls | `yolov8l-cls.pt` |
| YOLOv8x-cls | `yolov8x-cls.pt` |

</details>

## YOLO 可偵測類別清單（COCO 80 類）

本專案使用的 `yolov8*.pt` 預設是以 COCO 資料集訓練（共 80 類）。

<details>
<summary>展開：COCO 80 類別（英文＋中文）</summary>

| # | 類別（英文＋中文） |
|---:|---|
| 1 | person（人） |
| 2 | bicycle（自行車） |
| 3 | car（汽車） |
| 4 | motorcycle（機車） |
| 5 | airplane（飛機） |
| 6 | bus（公車） |
| 7 | train（火車） |
| 8 | truck（卡車） |
| 9 | boat（船） |
| 10 | traffic light（紅綠燈） |
| 11 | fire hydrant（消防栓） |
| 12 | stop sign（停止標誌） |
| 13 | parking meter（停車計時器） |
| 14 | bench（長椅） |
| 15 | bird（鳥） |
| 16 | cat（貓） |
| 17 | dog（狗） |
| 18 | horse（馬） |
| 19 | sheep（羊） |
| 20 | cow（牛） |
| 21 | elephant（大象） |
| 22 | bear（熊） |
| 23 | zebra（斑馬） |
| 24 | giraffe（長頸鹿） |
| 25 | backpack（後背包） |
| 26 | umbrella（雨傘） |
| 27 | handbag（手提包） |
| 28 | tie（領帶） |
| 29 | suitcase（行李箱） |
| 30 | frisbee（飛盤） |
| 31 | skis（滑雪板） |
| 32 | snowboard（單板滑雪板） |
| 33 | sports ball（運動球） |
| 34 | kite（風箏） |
| 35 | baseball bat（棒球棒） |
| 36 | baseball glove（棒球手套） |
| 37 | skateboard（滑板） |
| 38 | surfboard（衝浪板） |
| 39 | tennis racket（網球拍） |
| 40 | bottle（瓶子） |
| 41 | wine glass（酒杯） |
| 42 | cup（杯子） |
| 43 | fork（叉子） |
| 44 | knife（刀子） |
| 45 | spoon（湯匙） |
| 46 | bowl（碗） |
| 47 | banana（香蕉） |
| 48 | apple（蘋果） |
| 49 | sandwich（三明治） |
| 50 | orange（橘子） |
| 51 | broccoli（花椰菜） |
| 52 | carrot（胡蘿蔔） |
| 53 | hot dog（熱狗） |
| 54 | pizza（披薩） |
| 55 | donut（甜甜圈） |
| 56 | cake（蛋糕） |
| 57 | chair（椅子） |
| 58 | couch（沙發） |
| 59 | potted plant（盆栽） |
| 60 | bed（床） |
| 61 | dining table（餐桌） |
| 62 | toilet（馬桶） |
| 63 | tv（電視） |
| 64 | laptop（筆電） |
| 65 | mouse（滑鼠） |
| 66 | remote（遙控器） |
| 67 | keyboard（鍵盤） |
| 68 | cell phone（手機） |
| 69 | microwave（微波爐） |
| 70 | oven（烤箱） |
| 71 | toaster（烤麵包機） |
| 72 | sink（水槽） |
| 73 | refrigerator（冰箱） |
| 74 | book（書） |
| 75 | clock（時鐘） |
| 76 | vase（花瓶） |
| 77 | scissors（剪刀） |
| 78 | teddy bear（泰迪熊） |
| 79 | hair drier（吹風機） |
| 80 | toothbrush（牙刷） |

</details>

## 常見問題

**Q：無法開啟攝影機怎麼辦？**  
A：檢查 USB 攝影機連線，或嘗試變更 `cv2.VideoCapture()` 的編號參數（0, 1, 2...）。

**Q：模型下載緩慢？**  
A：首次執行時 Ultralytics 可能會下載權重，可先準備好對應 `.pt` 檔並放在專案目錄。

**Q：推論速度慢？**  
A：可先用 `01-gpu_cuda_test.py` 確認 GPU 是否可用，或改用 YOLOv8n（Nano）提升速度。


