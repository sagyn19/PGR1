import streamlit as st
import cv2
import numpy as np
from .utils import plot_histogram

"""
Module for Raster Operations.
Implements logic for convolution filters and histogram rendering.
"""

def render_filters_tab(original_image):
    st.header("Convolution Filters (Raster Algorithms)")
    
    col_controls, col_display = st.columns([1, 3])
    
    with col_controls:
        filter_mode = st.radio("Mode", ["Preset", "Custom Kernel"])
        
        if filter_mode == "Preset":
            kernel_type = st.selectbox("Choose Filter", ["Identity", "Gaussian Blur", "Sharpen", "Edge Detection"])
            kernels = {
                "Identity": np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
                "Gaussian Blur": np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16.0,
                "Sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
                "Edge Detection": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
            }
            selected_kernel = kernels[kernel_type]
        else:
            st.write("Edit Matrix (3x3):")
            # Create input grid for custom matrix
            matrix_inputs = []
            for r in range(3):
                cols = st.columns(3)
                row_vals = []
                for c in range(3):
                    # Default to 0 unless it's the center (1)
                    default = 1.0 if r == 1 and c == 1 else 0.0
                    val = cols[c].number_input(f"r{r}c{c}", value=default, key=f"k_{r}_{c}", label_visibility="collapsed")
                    row_vals.append(val)
                matrix_inputs.append(row_vals)
            selected_kernel = np.array(matrix_inputs)

        st.write("**Current Kernel:**")
        st.write(selected_kernel)

    with col_display:
        # Apply convolution
        filtered_image = cv2.filter2D(original_image, -1, selected_kernel)
        
        # Show results
        c1, c2 = st.columns(2)
        c1.image(original_image, caption="Original", use_container_width=True)
        c2.image(filtered_image, caption="Processed", use_container_width=True)
        
        st.divider()
        h1, h2 = st.columns(2)
        h1.pyplot(plot_histogram(original_image, "Original Histogram"))
        h2.pyplot(plot_histogram(filtered_image, "Processed Histogram"))