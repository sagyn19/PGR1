import streamlit as st
import cv2

"""
Module for Compression Simulation.
Handles JPEG encoding/decoding simulation.
"""

def render_compression_tab(original_image):
    st.header("Image Compression Simulation")
    
    quality = st.slider("JPEG Quality (1=Worst, 100=Best)", 1, 100, 95)
    
    # 1. Encode (Compress) to memory
    # We must convert RGB -> BGR for OpenCV encoding
    img_bgr = cv2.cvtColor(original_image, cv2.COLOR_RGB2BGR)
    success, encoded_img = cv2.imencode('.jpg', img_bgr, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    
    # 2. Calculate Size
    size_kb = len(encoded_img) / 1024
    
    # 3. Decode (Decompress) back to image
    decoded_img = cv2.imdecode(encoded_img, 1)
    decoded_img = cv2.cvtColor(decoded_img, cv2.COLOR_BGR2RGB)
    
    c1, c2 = st.columns(2)
    with c1:
        st.image(original_image, caption="Original (Lossless)", use_container_width=True)
    with c2:
        st.image(decoded_img, caption=f"Compressed (Q={quality})", use_container_width=True)
        st.metric("File Size", f"{size_kb:.2f} KB")
        
    if quality < 15:
        st.warning("⚠️ High compression creates visible 8x8 block artifacts.")