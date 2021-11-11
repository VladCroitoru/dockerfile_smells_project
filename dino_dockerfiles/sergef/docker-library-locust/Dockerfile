FROM sergef/docker-library-alpine:edge

EXPOSE 5557 5558 8089

COPY entrypoint.sh /entrypoint.sh

RUN apk add --no-cache \
    gcc \
    libzmq \
    musl-dev \
    python \
    python-dev \
    py-pip \
    zeromq-dev \
  && pip install \
    locustio \
  && chmod +x /entrypoint.sh

ENTRYPOINT ["tini", "--", "/entrypoint.sh"]
