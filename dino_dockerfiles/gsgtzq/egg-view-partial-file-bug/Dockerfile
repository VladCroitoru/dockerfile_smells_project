FROM node:carbon-alpine
LABEL MAINTAINER="zhangqi<gsgtzq@gmail.com>"
ENV NODE_ENV=prod
RUN apk update \
    && apk add tzdata \
    && rm -rf /var/cache/apk/*
COPY package.json /partial_file/package.json
WORKDIR /partial_file
RUN npm install
COPY . /partial_file
VOLUME [ "/partial_file/logs" ]
EXPOSE 7001
CMD [ "npm", "run", "start:docker" ]
