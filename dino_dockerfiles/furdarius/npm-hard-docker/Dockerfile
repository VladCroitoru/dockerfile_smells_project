# Npm Docker Container with python and build tools (make, gcc, ...)
# Base Dockerfile: furdarius/npm-docker
FROM furdarius/npm-docker

MAINTAINER furdarius <getlag@yandex.com>

# Packages
RUN apt-get update && apt-get install -y \
        build-essential \
        software-properties-common \
        python \
        python-dev \
        python-pip \
        python-virtualenv && \
    rm -rf /var/lib/apt/lists/*

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app

# Define default command.
ENTRYPOINT ["npm"]
CMD ["install"]
