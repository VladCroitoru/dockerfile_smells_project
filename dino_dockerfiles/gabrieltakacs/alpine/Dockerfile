FROM alpine:3.4
MAINTAINER Gabriel Takács <gtakacs@gtakacs.sk>

# Add repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.4/main' > /etc/apk/repositories && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.4/community' >> /etc/apk/repositories && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories && \
	echo 'http://dl-4.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories

# Install common utilities
RUN apk update && \
    apk upgrade -U && \
    apk add bash zsh vim git grep sed curl wget tar gzip pcre perl patch patchutils diffutils postfix openssh busybox-suid make g++

ADD ./bashrc /root/.bashrc

CMD ["/bin/bash"]
