import cv2
import numpy as np

def get_dominant_color(image):
    pixels = np.float32(image).reshape(-1, 3)
    n_colors = 5  # Number of dominant colors to extract
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    _, labels, centers = cv2.kmeans(pixels, n_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    dominant_color = centers[np.argmax(np.unique(labels, return_counts=True)[1])]
    return dominant_color

cap = cv2.VideoCapture(0)  # 0 for default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    roi = frame  # You can choose a specific region of interest if needed
    dominant_color = get_dominant_color(roi)

    color_display = np.zeros((100, 100, 3), dtype=np.uint8)
    color_display[:, :] = dominant_color

    cv2.imshow("Dominant Color Detection", color_display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
