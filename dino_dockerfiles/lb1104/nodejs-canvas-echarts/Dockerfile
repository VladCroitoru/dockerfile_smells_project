FROM alpine:3.7
RUN apk update && apk add build-base tzdata nodejs cairo-dev jpeg-dev pango-dev freetype-dev giflib-dev&& \
    cp -r -f /usr/share/zoneinfo/Asia/Chongqing /etc/localtime && \
    cd / && npm i -d canvas@1.6.9 echarts@3.8.5 underscore@1.8.3
