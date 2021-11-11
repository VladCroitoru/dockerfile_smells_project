# Use an official Python runtime as a parent image
FROM php:7.0-apache

COPY ./src /

RUN apt-get update && apt-get install -y \
    wakeonlan \
 && rm -rf /var/lib/apt/lists/*

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV USE_HTTPS="false" APPROVED_HASH="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" \
    MAX_PINGS="15" SLEEP_TIME="5" COMPUTER_NAME="computer1,computer2" \
    COMPUTER_MAC="00:00:00:00:00:00,00:00:00:00:00:00" COMPUTER_LOCAL_IP="192.168.0.1,192.168.0.2" \
    COMPUTER_SLEEP_CMD_PORT="7760" COMPUTER_SLEEP_CMD="suspend"
