FROM alpine:latest
MAINTAINER WangXian <xian366@126.com>

WORKDIR /app
ADD . .

RUN apk --update --no-progress add nodejs && rm -rf /app/.git

EXPOSE 3000
CMD npm start
