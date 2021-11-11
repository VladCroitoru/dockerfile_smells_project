#  dockopscenter
## OpsCenter in a docker

FROM alpine:3.3

MAINTAINER Alex Rudd <github.com/AlexRudd/dockopscenter/issues>

#OpsCenter Version
ARG OPSCENTER_VERSION=5.2.4

#install dependancies
RUN apk add --update tar
RUN apk add --update python
RUN apk add --update ca-certificates
RUN apk add --update openssh
RUN apk add --update openssl

# Download and extract OpsCenter
RUN mkdir -p /opt/opscenter
RUN wget -O - http://downloads.datastax.com/community/opscenter-$OPSCENTER_VERSION.tar.gz \
  | tar xzf - --strip-components=1 -C "/opt/opscenter";

# Add start script
COPY run_opscenter.py /
RUN chmod +x /run_opscenter.py

# Clean up
RUN apk del tar
RUN rm -rf /var/cache/apk/*

ENTRYPOINT ["/run_opscenter.py"]
