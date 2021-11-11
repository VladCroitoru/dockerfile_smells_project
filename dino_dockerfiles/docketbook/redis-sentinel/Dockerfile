FROM redis:3.2.3-alpine

MAINTAINER 	Dave Finster <davefinster@me.com>

RUN set -x \
	&& apk add --no-cache git curl \
	&& curl -vo /tmp/consul.zip https://releases.hashicorp.com/consul/0.7.0/consul_0.7.0_linux_amd64.zip \
	&& unzip /tmp/consul -d /usr/local/bin \
	&& rm /tmp/consul.zip \
	&& mkdir /config \
	&& curl -L -o containerpilot.tar.gz https://github.com/joyent/containerpilot/releases/download/2.4.1/containerpilot-2.4.1.tar.gz \
	&& tar -xzf containerpilot.tar.gz -C /usr/local/bin \
	&& rm -r containerpilot.tar.gz \
	&& curl -o sentinel-healthcheck.tar.gz https://manta.bne.blenco.net.au/davefinster/public/sentinel-healthcheck.tar.gz \
	&& tar -xzf sentinel-healthcheck.tar.gz -C /usr/local/bin \
	&& rm -r sentinel-healthcheck.tar.gz \
	&& chmod +x /usr/local/bin/sentinel-healthcheck

COPY ./redis-containerpilot.json /etc/containerpilot.json
COPY ./redis /data/redis
COPY ./sentinel /data/sentinel

EXPOSE 6379
EXPOSE 16379

ENV CONTAINERPILOT=file:///etc/containerpilot.json

ENTRYPOINT [ "/usr/local/bin/containerpilot", "redis-server", "/etc/redis.conf"]