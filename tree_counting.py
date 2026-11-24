
def count_trees(detections):

    if not detections:
        return 0

    return len(detections)


def get_tree_statistics(detections):

    total = count_trees(detections)

    if total == 0:
        return {
            "total_trees": 0,
            "average_confidence": 0
        }

    average_confidence = sum(
        tree["confidence"]
        for tree in detections
    ) / total

    return {
        "total_trees": total,
        "average_confidence": round(
            average_confidence, 3
        )
    }
