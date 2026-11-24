
import geopandas as gpd
from shapely.geometry import Point

def load_forest_boundary(file_path):

    return gpd.read_file(file_path)


def filter_trees_inside_boundary(
    detections,
    boundary,
    transform
):

    results = []

    boundary = boundary.to_crs(
        boundary.estimate_utm_crs()
    )

    polygon = boundary.geometry.union_all()

    for tree in detections:

        x1, y1, x2, y2 = tree["bbox"]

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        lon, lat = transform * (
            center_x, center_y
        )

        point = Point(lon, lat)

        if boundary.crs is not None:
            point_gdf = gpd.GeoSeries(
                [point], crs=boundary.crs
            ).to_crs(boundary.crs)

            if polygon.covers(point_gdf.iloc[0]):
                results.append(tree)

    return results


def calculate_tree_density(
    tree_count,
    area_hectares
):

    if area_hectares <= 0:
        return 0

    return tree_count / area_hectares
