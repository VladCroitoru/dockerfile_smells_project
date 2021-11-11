FROM debian:unstable

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install docker.io piuparts -y && rm -rf /var/lib/apt

# Support for docker:dind
ENV DOCKER_HOST=tcp://docker:2375
