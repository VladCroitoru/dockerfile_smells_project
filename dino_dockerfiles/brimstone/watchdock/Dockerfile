FROM ubuntu:14.04

MAINTAINER brimstone@the.narro.ws
CMD ["--dir", "/containers"]
VOLUME /containers

# TORUN -v /var/run/docker.sock:/var/run/docker.sock

ENV GOPATH /go

# Set our command
ENTRYPOINT ["/usr/local/bin/watchdock"]

# Install the packages we need, clean up after them and us
RUN apt-get update \
 && dpkg -l | awk '/^ii/ {print $2}' > /tmp/dpkg.clean \
 && apt-get install -y --no-install-recommends git golang ca-certificates \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists \

 && go get -v github.com/brimstone/watchdock \
 && mv $GOPATH/bin/watchdock /usr/local/bin/watchdock \

 && dpkg -l | awk '/^ii/ {print $2}' > /tmp/dpkg.dirty \
 && apt-get remove --purge -y $(diff /tmp/dpkg.clean /tmp/dpkg.dirty | awk '/^>/ {print $2}') \
 && rm /tmp/dpkg.* \
 && rm -rf $GOPATH
