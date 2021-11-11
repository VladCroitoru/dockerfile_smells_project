FROM node:alpine as base

LABEL maintainer "Martin Krutak <devklingac@gmail.com>"

# Update apk repositories
# Install chromium
# Minimize size
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories \
    && echo "http://dl-2.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && apk -U --no-cache \
    --allow-untrusted add \
    chromium \
    ttf-freefont \
    grep \
    && apk del --purge --force linux-headers binutils-gold gnupg zlib-dev libc-utils \
    && rm -rf /var/lib/apt/lists/* \
    /var/cache/apk/* \
    /usr/share/man \
    /tmp/* \
    /usr/lib/node_modules/npm/man \
    /usr/lib/node_modules/npm/doc \
    /usr/lib/node_modules/npm/html \
    /usr/lib/node_modules/npm/scripts

RUN mkdir -p /home/node/data  #; chown -R chrome:chrome /home/chrome/data

ENV HOME=/home/node CHROME_PATH=/usr/lib/chromium CHROME_BIN=/usr/bin/chromium-browser\
    OUTPUT_PATH=/home/node/data/ \
    CHROME_FLAGS="--headless --no-sandbox --disable-gpu" LIGHTHOUSE_FLAGS="--perf --disable-device-emulation --no-enable-error-reporting" \
    NODE_ENV=production

WORKDIR /home/node
USER node

FROM base as builder

USER node
COPY package.json yarn.lock ./
RUN yarn install --production

FROM base
WORKDIR /home/node
COPY --from=builder /home/node/node_modules/ ./node_modules/
COPY --from=builder /home/node/package.json /home/node/yarn.lock ./
ADD ./app/ /home/node/app/
CMD [ "npm", "start" ]
