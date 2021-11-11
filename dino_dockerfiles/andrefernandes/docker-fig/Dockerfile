# CentOS 7 + Fig

FROM andrefernandes/docker-centos7-base

MAINTAINER Andre Fernandes

RUN curl -L https://github.com/docker/fig/releases/download/0.5.2/linux > /usr/local/bin/fig && \
    chmod +x /usr/local/bin/fig

WORKDIR /app
VOLUME ["/app"]

# This container is a chrooted fig
ENTRYPOINT ["/usr/local/bin/fig"]
CMD ["--version"]

