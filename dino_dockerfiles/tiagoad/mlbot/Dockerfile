FROM python:3.7-alpine

# Set the environment variables
ENV BOT_STATE_FILE /state/status.dat
ENV RUN_INTERVAL 120

# Create the state directory
RUN mkdir /state

# Download requirements
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache bash

# Copy files
COPY bot.py .
COPY run.sh .

# Start container
CMD bash run.sh
