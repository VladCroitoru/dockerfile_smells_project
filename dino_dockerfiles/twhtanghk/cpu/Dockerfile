FROM node

ENV VER=${VER:-master} \
    REPO=https://github.com/twhtanghk/cpu \
    APP=/usr/src/app

WORKDIR $APP

RUN apt-get update && \
    apt-get clean && \
    git clone -b $VER $REPO $APP &&\
    npm install

ENTRYPOINT npm start
