FROM mhart/alpine-node:6

RUN apk --update --no-cache add git && \
    adduser hubot -h /home/hubot -D && \
    npm install -g coffee-script yo generator-hubot
