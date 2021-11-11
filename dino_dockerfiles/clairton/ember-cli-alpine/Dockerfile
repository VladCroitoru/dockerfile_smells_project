FROM node:alpine

MAINTAINER Clairton Rodrigo Heinzen <clairton.rodrigo@gmail.com>

RUN apk add --update --no-cache git

# Install ember-cli
RUN yarn global add ember-cli@3.14.0

# Allow SSH keys to be mounted (optional, but nice if you use SSH authentication for git)
VOLUME /root/.ssh

# Install chromium to run tests
RUN echo @edge http://nl.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
    echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories && \
    apk add --no-cache --update \
      chromium@edge \
      nss@edge

ENV DEBUG_PORT 5779

# test server on port 5779
EXPOSE 4200 7020 $DEBUG_PORT

# run ember server on container start
CMD ember server --live-reload-port $DEBUG_PORT --watcher polling --host 0.0.0.0
