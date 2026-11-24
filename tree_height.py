
import numpy as np
import rasterio

def analyze_tree_height(chm_file, detections):

    results = []

    with rasterio.open(chm_file) as src:

        chm = src.read(1)
        transform = src.transform
        nodata = src.nodata

        for i, tree in enumerate(detections, start=1):

            x1, y1, x2, y2 = map(int, tree["bbox"])

            # Convert image coordinates to raster coordinates
            # This assumes both images have the same dimensions
            # and alignment.
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(chm.shape[1], x2)
            y2 = min(chm.shape[0], y2)

            crop = chm[y1:y2, x1:x2]

            if crop.size == 0:
                continue

            valid = crop[np.isfinite(crop)]

            if nodata is not None:
                valid = valid[valid != nodata]

            if valid.size == 0:
                continue

            results.append({
                "tree_id": i,
                "estimated_height": float(np.max(valid))
            })

    return results
