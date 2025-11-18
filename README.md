# YOLOv8 物件偵測專案

本專案用於測試與演示 YOLOv8 物件偵測模型的基本功能，包括 GPU 環境驗證、模型配置檢查、即時攝影機捕捉及靜態影像推論。

## 專案檔案說明

### 1. `01-gpu_cuda_test.py`
**用途**：驗證 GPU 與 CUDA 環境  
**功能**：
- 檢查 PyTorch 版本
- 確認 GPU 是否可用
- 顯示 GPU 數量、CUDA 記憶體狀態及 cuDNN 版本

**執行方式**：
```bash
python 01-gpu_cuda_test.py
```

### 2. `02-檢查當前yolo配置.py`
**用途**：查看 YOLOv8 配置  
**功能**：
- 列出所有 YOLOv8 設定項目
- 顯示特定設定值（如 `runs_dir` 模型輸出目錄）

**執行方式**：
```bash
python 02-檢查當前yolo配置.py
```

### 3. `03-usb_webcam_test.py`
**用途**：即時攝影機畫面擷取與顯示  
**功能**：
- 開啟 USB 攝影機（預設編號 0）
- 讀取單一畫面後停留等待 ESC 按鍵
- 優雅退出時釋放攝影機資源

**執行方式**：
```bash
python 03-usb_webcam_test.py
```

**操作**：按 ESC 鍵退出

### 4. `04-picture_test.py`
**用途**：靜態影像物件偵測  
**功能**：
- 讀取本地影像檔案（預設 `bus.jpg`）
- 使用 YOLOv8m 模型進行物件偵測
- 在左上角顯示模型版本標示
- 顯示標註後的影像，等待 ESC 按鍵退出

**執行方式**：
```bash
python 04-picture_test.py
```

**操作**：按 ESC 鍵退出；視窗可自由調整大小

## 環境需求

- Python 3.8+
- PyTorch
- OpenCV (`opencv-python`)
- Ultralytics YOLOv8 (`ultralytics`)
- 裝有 NVIDIA GPU（建議但非必需）

## 模型檔案

- `yolov8m.pt`：YOLOv8 中等模型（Medium），約 49MB
- `bus.jpg`：用於測試的示範影像

## 快速開始

1. 確認 GPU 環境（可選）：
   ```bash
   python 01-gpu_cuda_test.py
   ```

2. 測試本地影像推論：
   ```bash
   python 04-picture_test.py
   ```

3. 測試實時攝影機：
   ```bash
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

## 授權

本專案用於教育與測試用途。

