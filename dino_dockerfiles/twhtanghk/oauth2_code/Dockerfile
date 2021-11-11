FROM node

ENV VER=${VER:-config} \
    REPO=https://github.com/twhtanghk/oauth2_code \
    APP=/usr/src/app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    git clone -b $VER $REPO $APP

WORKDIR $APP

RUN npm install
	
EXPOSE 1337

ENTRYPOINT node app.js --prod
