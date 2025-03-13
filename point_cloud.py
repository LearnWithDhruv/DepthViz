import numpy as np
import cv2
import plotly.graph_objects as go

def depth_to_3d(depth_map, focal_length=500):
    h, w = depth_map.shape
    fx, fy = focal_length, focal_length
    cx, cy = w // 2, h // 2

    x_points, y_points, z_points = [], [], []

    for v in range(h):
        for u in range(w):
            Z = depth_map[v, u]
            if Z > 0:  
                X = (u - cx) * Z / fx
                Y = (v - cy) * Z / fy
                x_points.append(X)
                y_points.append(Y)
                z_points.append(Z)

    return np.array(x_points), np.array(y_points), np.array(z_points)

def visualize_3d_point_cloud(x, y, z):
    """Interactive 3D visualization using Plotly."""
    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=2,
            color=z,  # Color based on depth
            colorscale='Jet',
            opacity=0.8
        )
    )])

    fig.update_layout(
        title="3D Point Cloud Visualization",
        scene=dict(
            xaxis_title="X Axis",
            yaxis_title="Y Axis",
            zaxis_title="Depth (Z Axis)"
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    return fig

# Example usage (Optional)
if __name__ == "__main__":
    depth_map = cv2.imread("output/depth_map.jpg", cv2.IMREAD_GRAYSCALE)
    x, y, z = depth_to_3d(depth_map)
    fig = visualize_3d_point_cloud(x, y, z)
    fig.show()
