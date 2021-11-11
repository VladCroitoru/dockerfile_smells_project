FROM node:10-slim

ENV NODE_ENV=production \
    GOSU_VERSION=1.10

RUN apt-get update \
    # Chrome
    && apt-get install -y \
        apt-transport-https \
        ca-certificates \
    && curl -sS https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y \
        google-chrome-stable \
    && rm -rf /var/lib/apt/lists/* \
    # GOSU
    && gpg --no-tty --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && export GOSU_URL="https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu -SL "${GOSU_URL}" \
    && curl -o /usr/local/bin/gosu.asc -SL "${GOSU_URL}.asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && mkdir -p /code

WORKDIR /code

ADD ./ ./

RUN yarn --frozen-lockfile

EXPOSE 3000

CMD [ "gosu", "node", "yarn", "start" ]
