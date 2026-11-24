
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")

DATA_DIR = os.path.join(BASE_DIR, "data")

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

DETECTION_DIR = os.path.join(OUTPUT_DIR, "detections")

MAP_DIR = os.path.join(OUTPUT_DIR, "maps")

REPORT_DIR = os.path.join(OUTPUT_DIR, "reports")

CONFIDENCE_THRESHOLD = 0.25

IOU_THRESHOLD = 0.5

IMAGE_SIZE = 640

SMALL_TREE_AREA = 1000

MEDIUM_TREE_AREA = 5000

for folder in [
    OUTPUT_DIR,
    DETECTION_DIR,
    MAP_DIR,
    REPORT_DIR
]:
    os.makedirs(folder, exist_ok=True)
