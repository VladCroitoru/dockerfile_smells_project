FROM node:16-alpine

RUN apk update --no-cache && \
    apk add git

RUN cd / && \
    git clone https://github.com/veteranmina/discord-bot && \
    cd discord-bot && \
    npm i && \
    npm run build

WORKDIR /discord-bot

ADD docker-entrypoint.sh /

CMD [ "/docker-entrypoint.sh" ]
