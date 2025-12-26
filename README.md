# YOLOv8 物件偵測專案

本專案展示如何使用 Ultralytics YOLOv8 進行物件偵測，包含 GPU 環境檢查、YOLO 設定查看、USB 攝影機即時畫面顯示，以及靜態影像推論。

測試環境：Windows 11 25H2、Python 3.10.19、PyTorch 2.9.1 + CUDA 13.0

## 專案檔案說明

### 1. `01-gpu_cuda_test.py`
**用途**：驗證 GPU 與 CUDA 環境  
**功能**：
- 檢查 PyTorch 版本
- 確認 GPU 是否可用
- 顯示 GPU 數量、CUDA 記憶體狀態及 cuDNN 版本

**執行方式**：
```pwsh
python 01-gpu_cuda_test.py
```

### 2. `02-檢查當前yolo配置.py`
**用途**：查看 YOLOv8 配置  
**功能**：
- 列出所有 YOLOv8 設定項目
- 讀取特定設定值（如 `runs_dir` 模型輸出目錄；目前程式只取值未額外列印）

**執行方式**：
```pwsh
python 02-檢查當前yolo配置.py
```

### 3. `03-usb_webcam_test.py`
**用途**：即時攝影機畫面擷取與顯示  
**功能**：
- 開啟 USB 攝影機（預設編號 0）並即時顯示畫面（連續更新）
- 可調整大小視窗（`cv2.WINDOW_NORMAL`）
- 退出時釋放攝影機資源並關閉視窗

**執行方式**：
```pwsh
python 03-usb_webcam_test.py
```

**操作**：按 `ESC` 或 `q` 退出（視窗需取得焦點）

### 4. `04-picture_test.py`
**用途**：靜態影像物件偵測  
**功能**：
- 讀取本地影像檔案（預設 `bus.jpg`）
- 使用 YOLOv8m 模型進行物件偵測
- 在左上角顯示使用的模型版本文字（目前為 `YOLOv8m`）
- 顯示標註後的影像，並停留等待 `ESC` 退出
- 視窗可自由調整大小（`cv2.WINDOW_NORMAL`）

**執行方式**：
```pwsh
python 04-picture_test.py
```

**操作**：按 `ESC` 鍵退出

### 5. `05-human_detect.py`
**用途**：使用 USB 攝影機進行人類（person）即時偵測與框選  
**功能**：
- 使用 `yolov8m.pt` 進行即時串流推論
- 僅偵測 COCO 類別中的 person（人類），並在畫面上框選
- 可調整大小視窗（`cv2.WINDOW_NORMAL`）
- 顯示模型名稱與 FPS

**執行方式**：
```pwsh
python 05-human_detect.py
```

**操作**：按 `ESC` 鍵退出

## 環境需求

- Python 3.8+
- PyTorch
- OpenCV (`opencv-python`)
- Ultralytics YOLOv8 (`ultralytics`)
- 裝有 NVIDIA GPU（建議但非必需）

## 模型檔案

- `yolov8m.pt`：YOLOv8 中等模型（Medium），約 49MB
- `bus.jpg`：用於測試的示範影像

## YOLO 可偵測類別清單（COCO 80 類）

本專案使用的 `yolov8*.pt` 預設是以 COCO 資料集訓練，常見的可偵測類別如下（共 80 類）：

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

## 快速開始

1. 確認 GPU 環境（可選）：
   ```pwsh
   python 01-gpu_cuda_test.py
   ```

2. 測試本地影像推論：
   ```pwsh
   python 04-picture_test.py
   ```

3. 測試實時攝影機：
   ```pwsh
   python 03-usb_webcam_test.py
   ```

## 專案特點

- ✅ 簡化的程式碼結構，易於理解與修改
- ✅ 完整的錯誤處理與資源清理
- ✅ 支援鍵盤中斷（Ctrl+C）
- ✅ 可調整大小的視窗界面
- ✅ 中文註解，適合學習

## 常見問題

**Q：無法開啟攝影機怎麼辦？**  
A：檢查 USB 攝影機連線，或嘗試變更 `cv2.VideoCapture()` 的編號參數（0, 1, 2...）

**Q：模型下載緩慢？**  
A：首次執行時 Ultralytics 會自動下載 `yolov8m.pt`，可預先至 Hugging Face 下載或指定本地路徑

**Q：推論速度慢？**  
A：檢查 `01-gpu_cuda_test.py` 確認 GPU 是否正常使用，或嘗試 YOLOv8n（Nano）以提升速度


