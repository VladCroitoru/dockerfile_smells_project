FROM node:7.7.3-slim
ENV \
  DEV_PACKAGES="git" \
  YARN_VERSION="0.22.0" \
  PATH=/root/.yarn/bin/:$PATH

RUN mkdir -p /var/log/orion \
  && curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version $YARN_VERSION \
  && apt-get update \
  && apt-get install -y --no-install-recommends $DEV_PACKAGES \
  && npm install -g hubot coffee-script \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/hubot
COPY package.json /opt/hubot
RUN yarn
COPY . /opt/hubot
COPY external-scripts.json /opt/hubot/external-scripts.json

CMD ["./bin/hubot", "--adapter", "slack"]
