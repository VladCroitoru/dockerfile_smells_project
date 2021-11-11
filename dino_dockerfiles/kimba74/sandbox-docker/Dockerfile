FROM ubuntu:14.04
MAINTAINER Steffen Krause <steffen.krause@soabridge.com>

# Setting user to root
USER root

# Create a directory
RUN mkdir -p /opt/sandbox

# Set the newly created directory as work directory
WORKDIR /opt/sandbox/

# Set the environment variable SNDBX_HOME
ENV SNDBX_HOME /opt/sandbox

# Setting labels on this image
LABEL com.soabridge.docker.container.name="Sandbox Docker" \
      com.soabridge.docker.container.version=0.1.4-SNAPSHOT

# Expose port 8090
EXPOSE 8090 9090

# Creating three volumes for the container
VOLUME ["/data/volume1", "/data/volume2", "/data/volume3"]

# Setting the entry point for the image (as per "best practices" the main command of the image)
ENTRYPOINT ["ping"] 

# Set default attributes for the command
CMD ["-h"]
