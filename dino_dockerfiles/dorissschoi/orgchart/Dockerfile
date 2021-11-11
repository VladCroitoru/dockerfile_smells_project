FROM node

ENV VER=${VER:-master} \
    REPO=https://github.com/ewnchui/orgchart \
    APP=/usr/src/app

WORKDIR $APP

RUN git clone -b $VER $REPO $APP \
&&  npm install

EXPOSE 1337

ENTRYPOINT ./entrypoint.sh
