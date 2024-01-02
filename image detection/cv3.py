import cv2
import pytesseract
from PIL import Image

# Step 1: Load the image using OpenCV
image_path = 'blur_image.jfif'  # Replace with the path to your image
image = cv2.imread(image_path)

# Step 2: Preprocess the image
resized_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply adaptive thresholding
adaptive_threshold_image = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=155, C=5
)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\natanana\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


# Step 4: Apply Tesseract OCR with custom configuration
custom_config = r'--psm 6'  # Page Segmentation Mode 6: Assume a single uniform block of text
text = pytesseract.image_to_string(adaptive_threshold_image, config=custom_config)
print(text)
cv2.imwrite('image4.png', adaptive_threshold_image)
cv2.imshow('Processed image', adaptive_threshold_image)
cv2.waitKey(0)
