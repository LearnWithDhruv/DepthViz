import streamlit as st
import cv2
import numpy as np
import plotly.graph_objects as go
from depth_model import estimate_depth
from point_cloud import depth_to_3d, visualize_3d_point_cloud

st.title("IMU-Based 3D Depth Mapping (Interactive)")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png"])

if uploaded_file is not None: 
    file_path = f"images/{uploaded_file.name}"
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(file_path, caption="Uploaded Image", use_column_width=True)

    st.write("### Generating Depth Map...")
    depth_map = estimate_depth(file_path)
    st.image("output/depth_map.jpg", caption="Depth Map", use_column_width=True)

    st.write("### Converting to 3D Point Cloud...")
    x, y, z = depth_to_3d(depth_map)

    # Display interactive 3D plot using Plotly
    fig = visualize_3d_point_cloud(x, y, z)
    st.plotly_chart(fig, use_container_width=True)

    st.success("Interactive 3D Point Cloud Generated! ✅")
