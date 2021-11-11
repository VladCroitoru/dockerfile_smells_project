# Use Python image
FROM python:3.8-slim-buster

# Add labels
LABEL MAINTAINER_NAME="Matthew Cale"  
LABEL MAINTAINER_EMAIL="mattc41190@gmail.com"

# Copy the dependency manifest to /app in the container
COPY ./requirements.txt /app/requirements.txt

# Set the WORKDIR to /app (all commands will be run from thsi context from here out)
WORKDIR /app

# Copy all file from diroectory to /app
COPY . /app

# Install requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose ports
EXPOSE 5050
EXPOSE 80
EXPOSE 443

# Create settable enviornment variables
ARG SCRIPT="run_dev.sh"
ENV PORT="5050"

# Run the start server command 
CMD sh $SCRIPT