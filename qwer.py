import gradio as gr
import cv2
import numpy as np
from PIL import Image
import io

# Define a function to read and process the uploaded image
def process_image(image):
    if isinstance(image, str):
        # If the input is a file path (when using Image(type="filepath"))
        img = cv2.imread(image)
    else:
        # If the input is the actual image data
        img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    
    if img is None:
        return "Failed to process the image."
    
    # Check if the image is grayscale
    if len(img.shape) == 2:
        return "Image is grayscale. Pixel values are not applicable."
    
    # Get the dimensions of the image
    height, width, _ = img.shape

    # Get pixel values for the top-left, top-right, bottom-left, and bottom-right pixels
    top_left = img[0, 0]
    top_right = img[0, width - 1]
    bottom_left = img[height - 1, 0]
    bottom_right = img[height - 1, width - 1]

    return f"Top Left Pixel: {top_left}, Top Right Pixel: {top_right}, Bottom Left Pixel: {bottom_left}, Bottom Right Pixel: {bottom_right}"

# Create a Gradio interface with an image input
iface = gr.Interface(
    fn=process_image,
    inputs=gr.inputs.Image(type="filepath"),  # Input type: Image file path
    outputs="text"  # Output type: text
)

# Launch the interface with the share option enabled
iface.launch(share=True)
