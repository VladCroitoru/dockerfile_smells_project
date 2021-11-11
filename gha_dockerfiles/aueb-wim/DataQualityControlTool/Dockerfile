# Use an official Python runtime as a parent image
FROM python:3.7-slim 
COPY requirements.txt setup.py README.md /
COPY mipqctool/ /mipqctool
RUN  apt-get update && \
     apt-get -y install libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info && \
     pip3 install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt && \
     pip3 install -e . 