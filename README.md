# RPS-1
The second block of code is where you should input the image path. Currently there is last_frame_path please change this to your image path. If you are using your web camera, then use the first block of code.

## How to Use
Please download the notebook as colab does not give a preview. You will then have access to all code in VS code or any other jupyter notebook. 
### 1. Using Your Webcam

Run the first block of code.
This will activate your webcam, capture a frame, and send it to the model for prediction.

### 2. Using a Saved Image (images are in the github above)

In the second block of code, replace:

image_path = last_frame_path


with the path to your own image, for example:

image_path = "my_image.jpg"


Then run the prediction cell.

That’s It

The model will output the detected move (Rock / Paper / Scissors) and the recommended counter-move.
