FROM node:10.11.0-alpine

WORKDIR /usr/src

COPY ["package.json", "package-lock.json", "/usr/src/"]

ENV NODE_ENV=production \
    PORT=3000 \
    LOG_LEVEL=info \
    TORRENT_DOMAIN=https://www.skytorrents.lol/

RUN npm i --loglevel=warn --progress=false --porcelain

COPY [".", "/usr/src/"]

EXPOSE 3000

CMD ["node", "."]
