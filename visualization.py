
import cv2
import numpy as np

def draw_detections(image, detections):

    result = np.array(image).copy()

    for i, tree in enumerate(detections, start=1):

        x1, y1, x2, y2 = map(
            int, tree["bbox"]
        )

        confidence = tree["confidence"]

        cv2.rectangle(
            result,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            result,
            f"Tree {i}: {confidence:.2f}",
            (x1, max(20, y1 - 5)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            1
        )

    return result


def create_count_chart(categories):

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.bar(
        list(categories.keys()),
        list(categories.values())
    )

    ax.set_title("Tree Size Distribution")
    ax.set_xlabel("Tree Category")
    ax.set_ylabel("Number of Trees")

    return fig
