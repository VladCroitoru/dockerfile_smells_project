FROM node:7-alpine
LABEL maintainer "syuchan1005 <syuchan.dev@gmail.com>"

RUN apk update && apk add ffmpeg curl && rm -rf /var/cache/apk/* \
    && curl -L -O https://github.com/syuchan1005/SoundME/archive/master.tar.gz \
    && tar xpvf master.tar.gz \
    && rm master.tar.gz \
    && mv SoundME-master data

WORKDIR data
RUN npm install

VOLUME /data/music
EXPOSE 80

CMD PORT=80 npm start
