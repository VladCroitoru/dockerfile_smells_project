# Base image
FROM phusion/baseimage:latest

# Update & upgrade system
RUN apt-get update && \
	apt-get upgrade -yq

# Install required packages
RUN apt-get install -yq wget ca-certificates

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
	sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
	apt-get update && \
	apt-get install -yq google-chrome-stable

# Install international fonts
RUN apt-get install -yq fonts-arphic-ukai fonts-arphic-uming fonts-ipafont-mincho fonts-ipafont-gothic fonts-unfonts-core

# Installation cleanup
RUN apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create data directory
RUN mkdir /data
WORKDIR /data

# Add chrome user
RUN addgroup chrome && \
	useradd -m -g chrome chrome
USER chrome

# Expose Chrome remote debugging port
EXPOSE 9222

ENTRYPOINT ["google-chrome", "--headless", "--disable-gpu"]