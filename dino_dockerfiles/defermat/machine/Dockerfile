FROM jpetazzo/dind
MAINTAINER defermat@defermat.net

# add machine
RUN wget https://github.com/docker/machine/releases/download/v0.1.0/docker-machine_linux-amd64
RUN chmod +x docker-machine_linux-amd64
RUN mv docker-machine_linux-amd64 /usr/bin/docker-machine

# Define additional metadata for our image.
VOLUME /var/lib/docker
CMD ["wrapdocker"]
