"""Windows CI verification: imports, DLL loading, detector, and GUI startup."""
import os
os.environ['QT_QPA_PLATFORM'] = 'offscreen'
import sys
from pathlib import Path
import numpy as np
import torch
import cv2
import depthai
from ultralytics import YOLO
from PyQt5.QtWidgets import QApplication

folder = Path(__file__).resolve().parent
model = YOLO(str(folder / 'tyre_detector.pt'))
result = model.predict(np.zeros((270,480,3), dtype=np.uint8), imgsz=480, verbose=False)
assert len(result) == 1
print('Torch:', torch.__version__, 'OpenCV:', cv2.__version__)
print('Model task:', model.task)
app = QApplication.instance() or QApplication([])
import TyreTrack_V4_8_2_overlay_options as tyretrack
window = tyretrack.Main()
assert window.overlay_mode_combo.count() == 3
window.close()
print('PASS: dependencies, model inference and PyQt GUI initialization')
