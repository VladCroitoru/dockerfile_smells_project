FROM node:0.10.33

# Install docker client
RUN apt-get update && apt-get install -y aufs-tools ca-certificates curl git iptables xz-utils

ENV DOCKER_VERSION 1.7.1

RUN curl -SL https://get.docker.io/builds/Linux/x86_64/docker-$DOCKER_VERSION -o /usr/bin/docker \
    && chmod +x /usr/bin/docker

# Uses the docker socket shared from the host machine
ENV DOCKER_HOST unix:///tmp/docker.sock

ADD . /usr/src/deployer
WORKDIR /usr/src/deployer
RUN npm install --unsafe-perm

CMD ["npm", "start"]
