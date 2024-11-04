import cv2
import numpy as np
from vidgear.gears import WriteGear

# Create a black screen
height, width = 720, 1280
black_screen = np.zeros((height, width, 3), dtype=np.uint8)

# Initialize WriteGear to save the video
output_params = {"-fourcc": "mp4v", "-fps": 30}
writer = WriteGear(output_filename="output.mp4", compression_mode=True, logging=True, **output_params)

# Define text properties
text = "Hello, World!"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 3
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = (width - text_size[0]) // 2
text_y = (height + text_size[1]) // 2

# Function to add text with alpha blending
def add_text_with_alpha(image, text, alpha):
    overlay = image.copy()
    cv2.putText(overlay, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)
    return cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

# Create frames with fading text
for alpha in np.linspace(0, 1, 30):  # Fade in
    frame = add_text_with_alpha(black_screen, text, alpha)
    writer.write(frame)

for alpha in np.linspace(1, 0, 30):  # Fade out
    frame = add_text_with_alpha(black_screen, text, alpha)
    writer.write(frame)

# Release resources
writer.close()
