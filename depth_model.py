import torch
import cv2
import numpy as np
from transformers import DPTForDepthEstimation, DPTImageProcessor

processor = DPTImageProcessor.from_pretrained("Intel/dpt-large")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

def estimate_depth(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    inputs = processor(images=image_rgb, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    
    depth = outputs.predicted_depth.squeeze().cpu().numpy()
    
    depth_rescaled = (depth - depth.min()) / (depth.max() - depth.min())
    depth_colormap = cv2.applyColorMap((depth_rescaled * 255).astype(np.uint8), cv2.COLORMAP_JET)

    cv2.imwrite("output/depth_map.jpg", depth_colormap)
    
    return depth
