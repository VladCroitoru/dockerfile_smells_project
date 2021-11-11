# Credit to: https://github.com/jpetazzo/dind

FROM ubuntu:vivid

# Let's start with some basic stuff.
#RUN apt-get update -qq && apt-get install -qqy apt-transport-https ca-certificates curl lxciptables
    
# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ | sh

# Install the magic wrapper.
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Define additional metadata for our image.
VOLUME /var/lib/docker
CMD ["wrapdocker"]

