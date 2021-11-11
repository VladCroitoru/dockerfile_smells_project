FROM ubuntu

# Install Docker signing key
RUN apt-key adv \
  --keyserver hkp://pgp.mit.edu:80 \
  --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

# Make sure we can install from https APT sources
RUN apt-get update && \
  apt-get install -y apt-transport-https && \
  rm -rf /var/lib/apt/lists/*

# Add the Docker APT source (which uses https, so needs to be after the above)
COPY docker.list /etc/apt/sources.list.d/docker.list

# Install Docker
RUN apt-get update && \
  apt-get install -y docker-engine curl && \
  rm -rf /var/lib/apt/lists/*

# Add Docker-in-Docker
ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034
RUN curl "https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" > /usr/local/bin/dind && \
  chmod +x /usr/local/bin/dind

# Custom scripts for forking Docker-in-Docker
ADD start-docker /usr/local/bin/start-docker
ADD stop-docker /usr/local/bin/stop-docker

# Make Drone auto-start Docker-in-Docker
ADD docker-helper.sh /etc/drone.d/docker-helper.sh
