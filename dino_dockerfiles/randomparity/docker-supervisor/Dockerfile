FROM ubuntu:trusty
MAINTAINER David Christensen <randomparity@gmail.com>

ENV BASE_LAST_UPDATE 2015-01-26

# Update image and install tools
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse" >> \
    /etc/apt/sources.list && \
    echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse" >> \
    /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get -q update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy install \
    software-properties-common supervisor wget git

# We've got everything we need so clear out the apt data
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/* && \
    rm -rf /tmp/*

# Configure image for supervisord operation
RUN mkdir -p /var/log/supervisor && \
    mkdir -p /etc/supervisor/conf.d

# Create a user to match the host OS for file access (e.g. network share)
ENV BASE_USER sysadmin
ENV BASE_GROUP sysadmin
ENV BASE_USER_UID 1000
ENV BASE_USER_GID 1000
RUN addgroup --gid $BASE_USER_GID $BASE_GROUP && \
    adduser --disabled-password --uid $BASE_USER_UID \
    --gid $BASE_USER_GID --gecos "" $BASE_USER

# Copy the supervisord configuration file into the container
COPY supervisor.conf /etc/supervisor.conf

# Users of this image SHOULD NOT specify "CMD" or "ENTRYPOINT" in 
# their Dockerfiles.
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor.conf" ]
