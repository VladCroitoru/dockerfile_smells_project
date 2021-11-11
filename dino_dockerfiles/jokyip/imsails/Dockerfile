FROM beevelop/cordova

ENV VER=${VER:-master} \
    REPO=https://github.com/twhtanghk/imsails \
    APP=/usr/src/app

RUN apt-get update && \
    apt-get install -y git imagemagick libav-tools python make g++ ffmpeg && \
    apt-get clean

RUN git clone -b $VER $REPO $APP

WORKDIR $APP

RUN npm install && \
    npm install -g ionic && \
    node_modules/.bin/bower --allow-root install && \
    node_modules/.bin/gulp plugin

EXPOSE 1337
        
ENTRYPOINT ./entrypoint.sh
