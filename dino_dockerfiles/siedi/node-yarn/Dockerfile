FROM node:7-alpine

RUN apk --no-cache add \
    git \
    ca-certificates \
    wget \
    bash \
    curl \
    tar \
    gnupg \
    python \
    build-base

RUN wget https://yarnpkg.com/install.sh \
    && chmod +x install.sh \
    && ./install.sh \
    && rm install.sh

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN apk --no-cache del \
    ca-certificates \
    wget \
    bash \
    curl \
    tar \
    gnupg

RUN rm -rf /root/.gnupg

ENV PATH /root/.yarn/bin:$PATH

