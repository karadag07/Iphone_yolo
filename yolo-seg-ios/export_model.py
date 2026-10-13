"""YOLO11n-seg modelini CoreML (.mlpackage) olarak disa aktarir."""
import shutil
from pathlib import Path

from ultralytics import YOLO

MODEL = "yolo11n-seg"  # daha dogru ama yavas: yolo11s-seg

model = YOLO(f"{MODEL}.pt")
out = model.export(format="coreml", imgsz=640, half=True)

dest = Path("Models") / f"{MODEL}.mlpackage"
dest.parent.mkdir(exist_ok=True)
if dest.exists():
    shutil.rmtree(dest)
shutil.copytree(out, dest)
print("Model hazir:", dest)
