FROM node:alpine
MAINTAINER Hong-Da, Ke

RUN apk update \
    && apk upgrade 

RUN apk add --no-cache git \
    && cd /root \
    && git clone https://github.com/LLK/scratch-gui.git \
    && cd scratch-gui \
    && npm install

WORKDIR /root/scratch-gui
EXPOSE 8601
CMD ["npm","start"]
