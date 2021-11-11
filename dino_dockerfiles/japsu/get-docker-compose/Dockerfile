FROM busybox
ENV DOCKER_COMPOSE_VERSION 1.13.0
ENV DOCKER_COMPOSE_SHA256 0d8af4d3336b0b41361c06ff213be5c42e2247beb746dbc597803e862af127e8
ENV SYSTEM Linux
ENV ARCH x86_64
ADD "https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-compose-$SYSTEM-$ARCH" /docker-compose
RUN echo "$DOCKER_COMPOSE_SHA256  /docker-compose" | sha256sum -c
CMD ["cat", "/docker-compose"]
