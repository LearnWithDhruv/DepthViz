import cv2
import os

def capture_image(output_path="images/captured_image.jpg"):
    cap = cv2.VideoCapture(2)  

    if not cap.isOpened():
        print("Error: Could not access webcam.")
        return None

    print("Press 'SPACE' to capture image, 'ESC' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow("Webcam - Press SPACE to Capture", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 32:  
            cv2.imwrite(output_path, frame)
            print(f"Image saved: {output_path}")
            break
        elif key == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()
    return output_path

if __name__ == "__main__":
    capture_image()
