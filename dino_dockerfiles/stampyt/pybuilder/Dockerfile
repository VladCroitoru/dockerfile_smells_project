FROM python:3.6.5-slim-jessie

# Install pip
RUN apt-get update
RUN apt-get install -y python3-pip\
	git
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 
RUN pip install --upgrade pip

RUN pip install pybuilder