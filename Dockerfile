FROM denismakogon/opencv3-slim:edge 

# Install opencv.
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --upgrade pip && pip3 install opencv-python

# Add our own code.
ADD frames.py /frames.py