FROM ubuntu:16.04

MAINTAINER didstopia

# Run a quick apt-get update/upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && DEBIAN_FRONTEND=noninteractive apt-get autoremove -y --purge

# Install dependencies, mainly for SteamCMD
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ca-certificates \
    software-properties-common \
    python-software-properties \
    libasound2 \
    xorg-dev \
    libx11-6 \
    libxcursor1 \
    libxinerama1 \
    libxrandr2 \
    libxi6 \
    libgl1-mesa-dev \
    curl \
    wget \
    xz-utils

# Run as root
USER root

# Setup the default timezone
ENV TZ=Europe/Helsinki
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setup the volume
RUN mkdir -p /factorio
VOLUME ["/factorio"]

# Install NodeJS (see below)
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

# Setup update checking support (web scraping)
ADD scraper/ /scraper/
WORKDIR /scraper
RUN npm install
WORKDIR /

# Setup scheduling support
ADD scheduler_app/ /scheduler_app/
WORKDIR /scheduler_app
RUN npm install
WORKDIR /

# Copy the Factorio scripts
ADD start_factorio.sh /start.sh
ADD check_autosave.sh /check_autosave.sh
ADD update_check.sh /update_check.sh

# Expose necessary ports
EXPOSE 34197/udp

# Setup default environment variables for the server
ENV FACTORIO_WORLD_NAME "docker"
ENV FACTORIO_SERVER_SETTINGS ""
ENV FACTORIO_PORT "34197"

# Cleanup
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean && DEBIAN_FRONTEND=noninteractive apt-get clean

# Start the server
ENTRYPOINT ["./start.sh"]
