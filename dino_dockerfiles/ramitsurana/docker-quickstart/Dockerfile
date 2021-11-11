# Dockerfile for docker image of Docker-quickstart

FROM ubuntu

MAINTAINER Ramit Surana "ramitsurana@gmail.com"

RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables
    
# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ | sh

# Install the magic wrapper.
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

RUN usermod -aG docker $USER
RUN docker run hello-world 

# Define additional metadata for our image.
VOLUME /var/lib/docker
CMD ["wrapdocker"]
