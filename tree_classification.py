
def classify_trees(detections):

    categories = {
        "Small": 0,
        "Medium": 0,
        "Large": 0
    }

    for tree in detections:

        x1, y1, x2, y2 = tree["bbox"]

        area = (x2 - x1) * (y2 - y1)

        if area < 1000:
            categories["Small"] += 1

        elif area < 5000:
            categories["Medium"] += 1

        else:
            categories["Large"] += 1

    return categories
