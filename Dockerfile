FROM python:3.8

# Install opencv.
RUN pip install opencv-python

# Add our own code.
ADD frames.py /frames.py