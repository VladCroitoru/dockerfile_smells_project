FROM node:alpine
ENV TARGET_VERSION=4.7.1
EXPOSE 80

RUN apk update && \
    apk upgrade && \
    apk add --no-cache rsync

ADD . /var/build/

WORKDIR /var/build/
# RUN cp drops/webchat-es5.js /var/build/02.babel-standalone/ && \
#     cp drops/webchat-es5.js /var/build/03.a.renderwebchat-using-es5-bundle/ && \
#     cp drops/webchat.js /var/build/03.b.renderwebchat-using-full-bundle/ && \
#     cp drops/webchat-minimal.js /var/build/03.c.renderwebchat-using-minimal-bundle/ && \
#     cp drops/webchat-es5.js /var/build/04.renderwebchat-with-react/ && \
#     cp drops/webchat-es5.js /var/build/05.renderwebchat-with-directlinespeech/

WORKDIR /var/build/01.create-react-app/
RUN npm ci && \
    npm install ../drops/botframework-directlinespeech-sdk-$TARGET_VERSION.tgz && \
    npm install ../drops/botframework-webchat-core-$TARGET_VERSION.tgz && \
    npm install ../drops/botframework-webchat-component-$TARGET_VERSION.tgz && \
    npm install ../drops/botframework-webchat-$TARGET_VERSION.tgz && \
    npm run build

WORKDIR /var/build/
RUN mkdir /var/artifacts && \
    mkdir /var/artifacts/gh-pages && \
    rsync -av . /var/artifacts/gh-pages/ --exclude 01.create-react-app && \
    rsync -av 01.create-react-app/build/ /var/artifacts/gh-pages/01.create-react-app/

WORKDIR /var/artifacts/gh-pages/
RUN npm install -g serve
ENTRYPOINT npx --no-install serve -p 80
