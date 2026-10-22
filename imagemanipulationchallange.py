
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("face1.jpg")

if image is None:
    print("Image not found!")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

cropped = image[50:250, 50:250]
cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)

bright = cv2.convertScaleAbs(image, alpha=1, beta=50)
bright_rgb = cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(bright_rgb)
plt.title("Brightened Image")
plt.axis("off")

plt.tight_layout()
plt.show()

cv2.imwrite("rotated.jpg", rotated)
cv2.imwrite("cropped.jpg", cropped)
cv2.imwrite("brightened.jpg", bright)

print("All images saved successfully!")
