# Using official python runtime base image
FROM python:2.7-slim

# Copy our code from the current folder to /app inside the container
ADD ./webapp /opt/app/
WORKDIR /opt/app

# Install our requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available for links and/or publish
EXPOSE 5000 

# Environment Variables
ENV DATADRIVEN_ENDPOINT data-driven.ukpds.org

# Define our command to be run when launching the container
CMD ["python", "app.py"]
