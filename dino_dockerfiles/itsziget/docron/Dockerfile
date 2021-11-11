ARG DOCKER_VERSION

FROM docker:${DOCKER_VERSION:-stable}

COPY start.sh /

RUN apk add --no-cache tzdata \
 && chmod +x /start.sh

ENTRYPOINT []

CMD ["/start.sh"]