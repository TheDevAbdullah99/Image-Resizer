import cv2

# Read the original image
img = cv2.imread("images.jpeg")

# Resize the image (example: 300x300)
resized_img = cv2.resize(img, (300, 300))

# Save as PNG (creates new file)
cv2.imwrite("resized_image.png", resized_img)

print("Image resized and converted to PNG successfully!")

scale_percent = 50  # reduce size to 50%
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized_img = cv2.resize(img, dim)
cv2.imwrite("resized_scaled.png", resized_img)
