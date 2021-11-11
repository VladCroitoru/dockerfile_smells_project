FROM alpine:3.5
MAINTAINER Daniel Olfelt <dolfelt@gmail.com>

# Install dependencies
RUN apk add --no-cache \
	bash \
	openssh \
	socat \
	&& rm -rf /var/cache/apk/*

# Copy entrypoint script to container
COPY entry.sh /entry.sh

# Setup environment variables; export SSH_AUTH_SOCK from socket directory
ENV SOCKET_DIR /.ssh-agent
ENV SSH_AUTH_SOCK ${SOCKET_DIR}/socket
ENV SSH_AUTH_PROXY_SOCK ${SOCKET_DIR}/proxy-socket

VOLUME ${SOCKET_DIR}

ENTRYPOINT ["/entry.sh"]

CMD ["ssh-agent"]
