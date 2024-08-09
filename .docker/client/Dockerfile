# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY client.py /app/client.py
COPY generate_random_512x512.py /app/generate.py

# Install the required packages
RUN pip install --no-cache-dir Pillow numpy termplotlib matplotlib requests

ENV IMAGE=/app/input.png
ENV URL="http://server-service/process-image"
ENV HISTOGRAM=/app/out/histogram.png

# Run the client
ENTRYPOINT python client.py --image=$IMAGE --url=$URL --histogram=$HISTOGRAM