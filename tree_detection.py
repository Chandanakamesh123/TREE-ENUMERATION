
from deepforest import main
import numpy as np

model = main.deepforest()
model.use_release()

def detect_trees(image):

    predictions = model.predict_image(
        image=np.asarray(image),
        return_plot=False
    )

    detections = []

    if predictions is None:
        return detections

    for _, row in predictions.iterrows():

        detections.append({
            "bbox": [
                float(row["xmin"]),
                float(row["ymin"]),
                float(row["xmax"]),
                float(row["ymax"])
            ],
            "confidence": float(row["score"])
        })

    return detections
