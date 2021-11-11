FROM node

ENV VER=${VER:-master} \
    REPO=https://github.com/twhtanghk/mobile \
    APP=/usr/src/app

WORKDIR $APP

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    git clone -b $VER $REPO $APP && \
    npm install

EXPOSE 1337

CMD node app.js --prod
