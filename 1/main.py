import cv2

# Replace 'path/to/your/image.jpg' with the actual path to your image file
image_path = "./Map.jpg"

# Read the image
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is not None:
    # Display the image (you may need to press a key to close the window)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
else:
    print(f"Error: Unable to read the image at '{image_path}'")
