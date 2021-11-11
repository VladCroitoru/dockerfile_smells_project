FROM node

ENV VER=${VER:-master} \
    REPO=https://github.com/twhtanghk/ssh \
    APP=/usr/src/app

RUN git clone -b $VER $REPO $APP

WORKDIR $APP

RUN npm install

EXPOSE 1337                                                                     
                                                                                
ENTRYPOINT ./entrypoint.sh
