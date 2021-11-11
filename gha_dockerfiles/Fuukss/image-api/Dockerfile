FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /image_service

# Set the working directory to /image_service
WORKDIR /image_service

# Copy the current directory contents into the container at /image_service
ADD . /image_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Fixed CV2. 2nd option. Sometimes works, sometimes not
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y