import streamlit as st
import cv2

"""
Module for Geometric Transformations.
Handles Affine transformations (Rotation/Scaling).
"""

def render_geometry_tab(original_image):
    st.header("Geometric Transformations")

    col_ctrl, col_disp = st.columns([1, 3])

    with col_ctrl:
        angle = st.slider("Rotation (°)", -180, 180, 0)
        scale = st.slider("Scale Factor", 0.1, 2.0, 1.0)
        st.info("Uses `cv2.getRotationMatrix2D` to build the Affine Matrix.")

    with col_disp:
        rows, cols, _ = original_image.shape
        center = (cols // 2, rows // 2)
        
        # Calculate Affine Matrix
        matrix = cv2.getRotationMatrix2D(center, angle, scale)
        
        # Apply Warp
        transformed = cv2.warpAffine(original_image, matrix, (cols, rows))
        
        st.image(transformed, caption=f"Rotated {angle}° / Scaled {scale}x", use_container_width=True)