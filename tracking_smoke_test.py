"""Exercise the same dynamic SciPy/Ultralytics tracker imports that failed in production."""
import numpy as np
import scipy
import scipy._cyutility
from scipy._lib import _ccallback_c
from ultralytics import YOLO
from pathlib import Path

print('SciPy version:', scipy.__version__)
model_path = Path(__file__).resolve().parent / 'tyre_detector.pt'
assert model_path.exists(), f'Missing detector: {model_path}'
model = YOLO(str(model_path))
frame = np.zeros((640, 640, 3), dtype=np.uint8)
# First track() call imports Ultralytics trackers, which import scipy.
results = model.track(source=frame, persist=True, verbose=False, device='cpu', tracker='bytetrack.yaml')
assert results is not None
print('PASS: YOLO model.track() and SciPy compiled modules imported successfully')
