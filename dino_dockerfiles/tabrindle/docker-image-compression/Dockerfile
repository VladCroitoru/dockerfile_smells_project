
FROM alpine:latest

WORKDIR /opt/google

RUN apk --no-cache add \
    bash \
    g++ \
    git \
    libpng-dev \
    libwebp-tools \
    make \
    openjpeg-tools

ARG VERSION="v1.0.1"

RUN git clone https://github.com/google/guetzli.git \
    --branch "${VERSION}" \
    --depth 1

RUN cd guetzli && make

COPY ./docker-entrypoint.sh /

WORKDIR /tmp

ENTRYPOINT ["/docker-entrypoint.sh"]
