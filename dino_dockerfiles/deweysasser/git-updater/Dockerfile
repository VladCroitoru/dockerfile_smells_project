FROM alpine:latest
MAINTAINER Dewey Sasser <dewey@deweysasser.com>

ARG DUMB_INIT_VERSION=1.2.5
# Purpose:  Periodically update a path
RUN apk add  --no-cache git gnupg rsync wget bash openssh-client
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_x86_64 && chmod +x /usr/local/bin/dumb-init
ADD run.sh /run.sh
ADD root /root

# How long to sleep between checks
ENV SLEEP 300

# false to skip signature check.  anything else to require signature
# all files in /keys will be importing to gpg to check signatures
ENV SIGNED false

# Place to copy the git files if signature checks
ENV TARGET /volume

# Location for the GPG import keys
ENV KEYS /keys

ENTRYPOINT [ "dumb-init", "/run.sh" ]
