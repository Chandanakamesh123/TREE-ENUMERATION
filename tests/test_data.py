
import os
import pandas as pd

def test_project_folders_exist():
    assert os.path.isdir("data")
    assert os.path.isdir("outputs")

def test_soil_data_exists():
    path = "data/soil_tests/soil_data.csv"
    assert os.path.isfile(path)

def test_soil_data_columns():
    path = "data/soil_tests/soil_data.csv"
    df = pd.read_csv(path)

    required_columns = [
        "location",
        "latitude",
        "longitude",
        "ph",
        "nitrogen",
        "phosphorus",
        "potassium",
        "organic_carbon"
    ]

    for column in required_columns:
        assert column in df.columns
