# IMU-Based 3D Depth Mapping (Interactive)

## Overview
This project performs depth estimation and 3D point cloud generation from images using deep learning. It leverages:

- **Streamlit** for interactive UI
- **OpenCV** for image processing
- **Hugging Face Transformers (DPT Model)** for depth estimation
- **Plotly** for 3D point cloud visualization

## Features
1. **Upload Image & Capture Image from Webcam**
2. **Generate Depth Map using Intel's DPT-Large Model**
3. **Convert Depth Map to 3D Point Cloud**
4. **Interactive 3D Visualization with Plotly**

## Project Structure

```
.
├── app.py               # Streamlit-based UI for depth estimation & 3D visualization
├── capture.py           # Webcam image capture script
├── depth_model.py       # Depth estimation using DPT-Large model
├── point_cloud.py       # Converts depth map to 3D points & visualizes it
├── images/              # Stores uploaded or captured images
├── output/              # Stores generated depth maps
└── README.md            # Documentation
```

---
## Dependencies

Ensure you have Python installed (preferably 3.8+). Install required libraries:

```bash
pip install streamlit opencv-python numpy torch transformers plotly
```

For GPU acceleration, install `torch` with CUDA support:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---
## Modules Explained

### 1. `app.py` (Streamlit UI)
- Allows users to **upload an image**
- Calls `estimate_depth()` to generate a **depth map**
- Converts depth to **3D point cloud**
- Displays an **interactive 3D visualization**

#### Key Functions:
- **File Handling**: Saves uploaded images to `images/`
- **Depth Estimation**: Calls `estimate_depth()` from `depth_model.py`
- **3D Point Cloud Conversion**: Calls `depth_to_3d()` and `visualize_3d_point_cloud()`

### 2. `capture.py` (Webcam Image Capture)
- Uses **OpenCV** to capture an image from the webcam
- Saves the image in `images/`

#### Key Features:
- Press `SPACE` to **capture an image**
- Press `ESC` to **exit**

### 3. `depth_model.py` (Depth Estimation)
- Uses **Intel's DPT-Large Model** for depth estimation
- Converts an image into a **grayscale depth map**
- Saves the depth map in `output/`

#### Key Functions:
- **estimate_depth(image_path)**: 
  - Loads image with OpenCV
  - Converts to RGB and processes using **DPT-Large Model**
  - Normalizes depth values
  - Saves as a colormap (`output/depth_map.jpg`)

### 4. `point_cloud.py` (3D Point Cloud Processing)
- Converts **depth map to 3D coordinates**
- Uses **Plotly** for interactive **3D visualization**

#### Key Functions:
- **depth_to_3d(depth_map, focal_length=500)**:
  - Converts **pixel depth values to real-world 3D points**
  - Uses focal length to reconstruct depth
- **visualize_3d_point_cloud(x, y, z)**:
  - Uses **Plotly** to render an **interactive scatter plot**

---
## Running the Application

### 1. Start the Streamlit App
```bash
streamlit run app.py
```

### 2. Capture Image from Webcam
```bash
python capture.py
```

### 3. Manually Generate Depth & 3D Point Cloud
```python
from depth_model import estimate_depth
from point_cloud import depth_to_3d, visualize_3d_point_cloud
import cv2

# Estimate depth
image_path = "images/sample.jpg"
depth_map = estimate_depth(image_path)

# Convert to 3D
x, y, z = depth_to_3d(depth_map)
fig = visualize_3d_point_cloud(x, y, z)
fig.show()
```

---
## Expected Outputs

### Uploaded Image & Depth Map
- The application will display the **original image** and the **computed depth map**

### Interactive 3D Point Cloud
- **Colored scatter plot** representing depth in 3D space
- Rotate, zoom, and pan using **Plotly's interactive controls**

---
## Troubleshooting

| Issue | Solution |
|--------|-----------|
| `cv2.VideoCapture(2)` not working | Change camera index to `0` or `1` |
| Depth map not generated | Ensure `output/` exists & model is correctly installed |
| No 3D visualization | Check if `depth_map.jpg` is being created |

---
## Future Improvements
- **Support for Real-Time Video Depth Estimation**
- **Integration with LiDAR / IMU Data for Accuracy**
- **Optimize Depth Processing with Faster Models**

---
## Credits
- **Intel DPT-Large Model** from Hugging Face
- **OpenCV** for Image Processing
- **Streamlit** for Interactive UI
- **Plotly** for 3D Visualization
