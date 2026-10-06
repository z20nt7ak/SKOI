import cv2
import time

start = time.perf_counter()
image = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)
result = cv2.magnitude(sobel_x, sobel_y)
result = cv2.convertScaleAbs(result)
cv2.imwrite("result_opencv.jpeg", result)
end = time.perf_counter()
print("OpenCV:", end - start, "секунд")