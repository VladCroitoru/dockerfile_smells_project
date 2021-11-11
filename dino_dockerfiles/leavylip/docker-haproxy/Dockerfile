# Leavylip HAProxy public-facing load balancer
# Based on / inspired by:
#   https://hub.docker.com/r/yaronr/haproxy-confd/
#   https://hub.docker.com/r/frolvlad/alpine-oraclejdk8/
#   https://hub.docker.com/r/jihchi/alpine-confd/

# Use the minimal alpine base image
FROM gliderlabs/alpine:3.2
MAINTAINER LeavyLip <dev@leavylip.com>

# Set configuration variables
ENV ETCD_NODE 172.17.42.1:4001
ENV CONFD_VERSION 0.10.0

# Install HAProxy
RUN apk-install haproxy bash

# Install Confd
ADD https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 \
	/bin/confd
RUN chmod u+x /bin/confd

# Add files
ADD entrypoint.sh /entrypoint.sh
ADD confd /etc/confd

# Expose ports. 8080 => main port; 9000 => stats port.
EXPOSE 8080
EXPOSE 9000

# Set entrypoint.sh as starting executable
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["/entrypoint.sh"]

