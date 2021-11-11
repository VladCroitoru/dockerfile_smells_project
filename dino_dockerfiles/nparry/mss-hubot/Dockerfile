FROM node:7

RUN adduser --system --shell /bin/bash hubot
RUN mkdir -p /usr/local/lib/hubot

COPY . /usr/local/lib/hubot/
WORKDIR /usr/local/lib/hubot/
RUN git rev-parse HEAD > VERSION
RUN rm -rf .git
RUN [ ! -d node_modules ] || rm -rf node_modules
RUN mkdir node_modules && chown hubot:users node_modules

USER hubot
RUN npm install

ENTRYPOINT [ "./bin/hubot" ]

