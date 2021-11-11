# Notelist 0.9.4 Dockerfile - Jose A. Jimenez (jajimenezcarm@gmail.com)
#
# How to build the Docker image:
#     docker image build -t notelist .
#
# See the "README.md" file for more information.

# Base image
FROM python:3.9.0-slim

# Set working directory
WORKDIR /tmp

# Update the APT index and delete APT temporary files
RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Install the Wheel Python package
RUN pip install --no-cache-dir wheel

# Copy Notelist source files
COPY . .

# Delete package directories if they exist
RUN rm -rf *.egg-info build dist

# Generate Notelist wheel package, install it, install production Python
# libraries and delete Notelist source files.
RUN python setup.py bdist_wheel && \
    pip install --no-cache-dir ./dist/notelist-* && \
    pip install --no-cache-dir -r requirements_pro.txt && \
    rm -rf *

# Set Flask environment variable
ENV FLASK_APP=notelist

# Set working directory
WORKDIR /

# Run the Gunicorn WSGI web server for Notelist listening on port 5000
ENV ACCESS_LOG=/usr/src/access.log
ENV ERROR_LOG=/usr/src/error.log

EXPOSE 5000
CMD gunicorn -b 0.0.0.0:5000 \
    --access-logfile $ACCESS_LOG \
    --error-logfile $ERROR_LOG \
    notelist:app
