FROM node:0.10-slim

ENV APP_DIRECTORY /curvytron

WORKDIR ${APP_DIRECTORY}

COPY bower-resolutions.json /bower-resolutions.json

RUN apt-get update && \
    apt-get install -y \
        git \
        python \
        make \
        g++ && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/*

RUN git clone https://github.com/Curvytron/curvytron.git ${APP_DIRECTORY} && \
    npm install -g json bower gulp && \
    npm install json -g && \
    cat ${APP_DIRECTORY}/bower.json /bower-resolutions.json | json --merge > ${APP_DIRECTORY}/bower-tmp.json && \
    mv ${APP_DIRECTORY}/bower-tmp.json ${APP_DIRECTORY}/bower.json && \
    rm /bower-resolutions.json && \
    npm install && \
    bower install --allow-root && \
    gulp

EXPOSE 8080

CMD node bin/curvytron.js
