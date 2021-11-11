# Use Ubuntu 14.04 (Same base as CircleCI Builders)
FROM ubuntu:14.04

# Define Maintainer
MAINTAINER Ethan Pursley <ethan.k.pursley@gmail.com>

# Set Default PHP Version
ENV PHP_VERSION 7.1.0

# Install Dependencies required for PHP Builds
RUN apt-get update && \
    apt-get install -y git curl build-essential libxml2-dev \
    libcurl4-gnutls-dev libjpeg-dev libpng12-dev libmcrypt-dev libssl-dev \
    libreadline-dev libtidy-dev libxslt1-dev autoconf re2c bison && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    useradd -ms /bin/bash ubuntu && \
    su ubuntu -c 'curl -L http://git.io/phpenv-installer | bash'

# Switch to ubuntu user
USER ubuntu

# Set workdir
WORKDIR /home/ubuntu

# Set Environment PATH
ENV PATH /home/ubuntu/.phpenv/bin:/home/ubuntu/.phpenv/shims:$PATH

# Copy build script to container
COPY build-php.sh ./build-php.sh

# Run build script
CMD ["./build-php.sh"]
