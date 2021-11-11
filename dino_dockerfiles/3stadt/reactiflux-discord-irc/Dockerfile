FROM node:7-alpine
LABEL author="3stadt <docker@3stadt.com>"
ENV REFRESHED_AT 2018-12-23_02

RUN apk update && apk upgrade \
    && apk add --no-cache git openssh \
    && addgroup -S discordirc \
    && adduser -S -g discordirc discordirc \
    && mkdir -p /home/discordirc/app\
    && chown -R discordirc:discordirc /home/discordirc
USER discordirc
WORKDIR /home/discordirc/app
RUN git clone -b 'v2.6.2' \
    --single-branch --depth 1 https://github.com/reactiflux/discord-irc.git . \
    && npm install && npm run build \
    && mkdir /home/discordirc/config

CMD []
ENTRYPOINT ["npm", "start", "--", "--config", "/home/discordirc/config/config.json"]
