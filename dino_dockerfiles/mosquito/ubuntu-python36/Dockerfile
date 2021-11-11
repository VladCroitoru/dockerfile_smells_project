FROM ubuntu:17.10

# Upgrade the system
RUN apt-get update && apt-get upgrade -y

# Install python
RUN apt-get install -y python3 python3-pip python3-virtualenv make

# Install compiller
RUN apt-get install -y build-essential git

# Install headers for useful libraries
RUN apt-get install -y \
    libacl1-dev \
    libfreetype6-dev \
    libgdal-dev \
    libgif-dev \
    libjpeg-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libpng-dev \
    libpq-dev \
    libssl-dev \
    libtiff5-dev \
    libwebp-dev \
    tcl-dev \
    tk-dev \
    zlib1g-dev

# Configure locales
RUN apt-get install -f locales
RUN locale-gen en_US.UTF-8 ru_RU.UTF-8

ENV LANG ru_RU.UTF-8

