import cv2

image = cv2.imread('apple.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image,(224,224))

cv2.imshow('Processed Image', resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(f"processed image shape: {resized_image.shape}")