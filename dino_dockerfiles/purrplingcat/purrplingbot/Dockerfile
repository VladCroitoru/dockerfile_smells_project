FROM node:12.16.1-buster-slim AS builder

RUN mkdir -p /build

WORKDIR /build

RUN apt-get update &&\
    apt-get install -y git --no-install-recommends &&\
    rm -rf /var/lib/apt/lists/*

COPY . /build

RUN yarn && yarn build

FROM node:12.16.1-buster-slim

LABEL com.purrplingcat.name="PurrplingBot"
LABEL com.purrplingcat.version="2.0.0"
LABEL com.purrplingcat.vendor="PurrplingCat"
LABEL com.purrplingcat.email="dev@purrplingcat.com"
LABEL com.purrplingcat.github="https://github.com/PurrplingCat/PurrplingBot"

ENV DEBUG=0
ENV APP_DIR="/opt/PurrplingBot"
ENV APP_CONFIG_DIR="/data/config"
ENV PATH=$APP_DIR/bin:$PATH

# Install binary dependencies
RUN apt-get update &&\
    apt-get install -y git --no-install-recommends &&\
    rm -rf /var/lib/apt/lists/*

# Create app place
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

# Copy bundle, install main&plugin deps
COPY --from=builder /build/package.json .
COPY --from=builder /build/.yarnrc .
COPY --from=builder /build/yarn.lock .
COPY --from=builder /build/dist/ dist/
COPY --from=builder /build/bin/ bin/
COPY --from=builder /build/data/ data/
RUN yarn --production

# Redirect configs to /data/config
RUN ln -s $APP_CONFIG_DIR config

VOLUME /data/config

# Start PurrplingBot
CMD ["yarn", "start"]
