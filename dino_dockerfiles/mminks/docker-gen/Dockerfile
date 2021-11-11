FROM alpine:latest

LABEL maintainer="Meik Minks <mminks@inox.io>"

ENV DOCKER_HOST unix:///tmp/docker.sock

RUN apk add --no-cache openssl curl jq bash python bind-tools

RUN wget -q https://github.com/barnybug/cli53/releases/download/$(curl -L -s -H 'Accept: application/json' https://github.com/barnybug/cli53/releases/latest | sed -e 's/.*"tag_name":"\([^"]*\)".*/\1/')/cli53-linux-386 -O /usr/local/bin/cli53
RUN chmod +x /usr/local/bin/cli53

RUN wget -q https://github.com/jwilder/docker-gen/releases/download/$(curl -L -s -H 'Accept: application/json' https://github.com/jwilder/docker-gen/releases/latest | sed -e 's/.*"tag_name":"\([^"]*\)".*/\1/')/docker-gen-alpine-linux-amd64-$(curl -L -s -H 'Accept: application/json' https://github.com/jwilder/docker-gen/releases/latest | sed -e 's/.*"tag_name":"\([^"]*\)".*/\1/').tar.gz -O /tmp/docker-gen-alpine-linux-amd64.tar.gz
RUN tar -xzvf /tmp/docker-gen-alpine-linux-amd64.tar.gz -C /usr/local/bin

RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN pip install awscli

RUN rm -rf /var/cache/apk/* /tmp/*

ENTRYPOINT ["/usr/local/bin/docker-gen"]

