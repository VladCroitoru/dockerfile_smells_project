#
# Docker Base image for Python 3.8 with Rtree and Shapely
#

FROM python:3.8-slim
# Copy our own application
WORKDIR /app
COPY . /app
# Proceed to install the requirements...do
RUN apt-get update && \
    apt-get install libspatialindex-dev -y && \
    pip install -r requirements_production.txt
