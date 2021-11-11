# Run retroframes
FROM node:12.16.3-alpine
LABEL maintainer="michel@micheldebree.nl"
RUN apk add --no-cache  ca-certificates=20191127-r2 ffmpeg=4.2.1-r3 \
 && rm -rf /var/cache/*
COPY /app/ /retroframes/
WORKDIR /retroframes
RUN yarn install
WORKDIR /data
ENTRYPOINT ["node", "/retroframes/index.js"]
