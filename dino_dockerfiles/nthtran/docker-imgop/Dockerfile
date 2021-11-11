FROM nthtran/iojs-libvips:7.42.3

ADD . /src
WORKDIR /src

RUN npm i

EXPOSE 3000
CMD node_modules/.bin/pm2 start index.js -i 0 && \
    node_modules/.bin/pm2 logs
