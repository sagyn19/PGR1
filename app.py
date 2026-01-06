import streamlit as st
import numpy as np
import cv2
from tabs import filters, geometry, compression

"""
Main module for the PGR1 application.
This file initializes the Streamlit interface and loads individual
modules for filters, geometry, and compression.

"""

# Page Config
st.set_page_config(page_title="PGR1 Graphics Project", layout="wide")

# Sidebars
st.sidebar.title("PGR1 Project")
st.sidebar.info("Topics: Raster Algos, Geometry, Compression")
uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# Main App Logic
if uploaded_file is not None:
    # Load Image properly
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    original_image = cv2.imdecode(file_bytes, 1)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    
    st.title("Digital Image Processing Workbench")
    
    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["Filters & Histograms", "Geometry", "Compression"])
    
    with tab1:
        filters.render_filters_tab(original_image)
    with tab2:
        geometry.render_geometry_tab(original_image)
    with tab3:
        compression.render_compression_tab(original_image)

else:
    st.title("Welcome")
    st.write("Please upload an image in the sidebar to begin.")