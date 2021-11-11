FROM node:6.12.3-alpine
RUN apk add --no-cache bash python git make gcc g++ tzdata &&\
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
    npm install -g grunt &&\
    npm install -g node-gyp &&\
    git clone https://github.com/electron/mini-breakpad-server.git &&\
    cd /mini-breakpad-server &&\
    npm install . &&\
    grunt &&\
    apk del python git make gcc g++ tzdata &&\
    rm -rf /mini-breakpad-server/.git
EXPOSE 1127
CMD ["node", "/mini-breakpad-server/lib/app.js"]
