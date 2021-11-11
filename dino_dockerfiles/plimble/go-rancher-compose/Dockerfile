FROM golang:latest

ENV RANCHER_COMPOSE_VERSION v0.9.0

RUN apt-get update -q \
	&& apt-get upgrade -y -q \
	&& apt-get install -y -q --no-install-recommends ca-certificates tar wget curl \
	&& wget -O /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz "https://github.com/rancher/rancher-compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz" \
	&& tar -xf /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz -C /tmp \
	&& mv /tmp/rancher-compose-${RANCHER_COMPOSE_VERSION}/rancher-compose /usr/local/bin/rancher-compose \
	&& rm -R /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz /tmp/rancher-compose-${RANCHER_COMPOSE_VERSION}\
	&& chmod +x /usr/local/bin/rancher-compose \
  && curl https://glide.sh/get | sh \
	&& go get github.com/tools/godep

# Cleanup image
RUN apt-get autoremove -y -q
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /var/tmp/*
