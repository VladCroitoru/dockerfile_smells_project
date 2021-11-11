FROM node:latest

RUN apt-get update && \
    apt-get install -qqy \
    vim \
    locales \
    git \
    python \
    build-essential \
    libssl-dev \
    curl

RUN mkdir -p /tmp/build
WORKDIR /tmp/build
RUN curl -L https://github.com/wg/wrk/archive/3.1.0.tar.gz | tar zx --strip 1 && make && cp ./wrk /usr/bin/wrk

CMD ["node"]
