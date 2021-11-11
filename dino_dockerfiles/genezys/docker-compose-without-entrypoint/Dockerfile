FROM debian:9.3

MAINTAINER Vincent Robert <vincent.robert@genezys.net>

ENV \
	DEBIAN_FRONTEND="noninteractive" \
	DOCKER_VERSION="17.12.0-ce" \
 	COMPOSE_VERSION="1.18.0"

RUN apt-get update -q \
	&& apt-get install -y -q --no-install-recommends curl ca-certificates \
	&& curl -o /tmp/docker.tgz -L \
		"https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz" \
  && tar xvzf /tmp/docker.tgz -C /usr/local/bin --strip-components=1 \
  && rm /tmp/docker.tgz \
	&& curl -o /usr/local/bin/docker-compose -L \
		"https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-Linux-x86_64" \
	&& chmod +x /usr/local/bin/docker-compose

WORKDIR /app
ENTRYPOINT []
CMD ["/bin/bash"]
