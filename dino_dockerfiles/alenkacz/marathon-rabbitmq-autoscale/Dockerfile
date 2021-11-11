FROM java:8u66-jdk
MAINTAINER varkockova.a@gmail.com

ARG version=1.0-SNAPSHOT

# install Docker
ENV DOCKER_VERSION=1.10.3
RUN curl -sSL -O https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION} \
    && chmod +x docker-${DOCKER_VERSION} \
    && mv docker-${DOCKER_VERSION} /usr/local/bin/docker

# install docker-compose
ENV COMPOSE_VERSION 1.6.2
RUN curl -o /usr/local/bin/docker-compose -L "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-Linux-x86_64" \
	&& chmod +x /usr/local/bin/docker-compose

COPY . /autoscale
WORKDIR /autoscale
RUN ./gradlew distTar

RUN tar -xvf ./build/distributions/autoscale-$version.tar -C /var

WORKDIR /var/autoscale-$version/bin

ENTRYPOINT ["./autoscale"]