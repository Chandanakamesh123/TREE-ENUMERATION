
import streamlit as st
import pandas as pd

from tree_detection import detect_trees
from tree_counting import count_trees
from tree_classification import classify_trees
from visualization import draw_detections
from report_generation import generate_csv
from utils.image_processing import preprocess_image

st.set_page_config(
    page_title="Tree Enumeration System",
    page_icon="🌳",
    layout="wide"
)

st.title("🌳 AI-Based Tree Enumeration System")

st.markdown("""
Detect, count and analyze individual trees
from drone and satellite imagery.
""")

uploaded_file = st.file_uploader(
    "Upload Drone/Satellite Image",
    type=["jpg", "jpeg", "png", "tif", "tiff"]
)

if uploaded_file:

    image = preprocess_image(uploaded_file)

    st.subheader("Input Image")
    st.image(image, use_container_width=True)

    if st.button("Start Tree Enumeration"):

        with st.spinner("Detecting trees..."):

            detections = detect_trees(image)

            total = count_trees(detections)

            classification = classify_trees(detections)

            result = draw_detections(image, detections)

        st.subheader("Detection Result")
        st.image(result, use_container_width=True)

        col1, col2 = st.columns(2)

        col1.metric("Total Trees", total)

        col2.metric(
            "Detection Confidence",
            f"{sum(d['confidence'] for d in detections)/total:.2%}"
            if total else "N/A"
        )

        st.subheader("Tree Size Classification")
        st.json(classification)

        csv_data = generate_csv(detections)

        st.download_button(
            "Download Tree Enumeration CSV",
            data=csv_data,
            file_name="tree_report.csv",
            mime="text/csv"
        )
