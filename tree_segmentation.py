
import cv2
import numpy as np

def segment_trees(image, detections):

    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    masks = []

    for tree in detections:

        x1, y1, x2, y2 = map(
            int, tree["bbox"]
        )

        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(img.shape[1], x2)
        y2 = min(img.shape[0], y2)

        crop = gray[y1:y2, x1:x2]

        if crop.size == 0:
            continue

        _, mask = cv2.threshold(
            crop, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        masks.append({
            "bbox": [x1, y1, x2, y2],
            "mask": mask
        })

    return masks
