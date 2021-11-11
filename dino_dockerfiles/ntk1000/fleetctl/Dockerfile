FROM gliderlabs/alpine:latest
MAINTAINER ntk1000

ENV FLEET_VERSION=0.11.5

ADD https://github.com/coreos/fleet/releases/download/v${FLEET_VERSION}/fleet-v${FLEET_VERSION}-linux-amd64.tar.gz /tmp/fleet.tar.gz

RUN cd /bin \
	&& tar zxvf /tmp/fleet.tar.gz \
	&& mv ./fleet-v${FLEET_VERSION}-linux-amd64/* ./ \
	&& chmod +x /bin/fleetctl \
	&& rm /tmp/fleet.tar.gz \
	&& rm -rf ./fleet-v${FLEET_VERSION}-linux-amd64

ENTRYPOINT ["/bin/fleetctl"]
