FROM alpine:3.4

RUN apk add --no-cache avahi bash openssl \
  && rm -rf /etc/avahi/services/*

# Install forego.
ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego /usr/local/bin/forego
RUN chmod u+x /usr/local/bin/forego

# Install docker-gen.
ENV DOCKER_GEN_VERSION 0.7.3

RUN wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
  && tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
  && rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz

ADD avahi-daemon.conf /etc/avahi/avahi-daemon.conf
ADD data/ /opt/app

WORKDIR /opt/app

ENV DOCKER_HOST unix:///tmp/docker.sock

CMD ["forego", "start", "-r"]
