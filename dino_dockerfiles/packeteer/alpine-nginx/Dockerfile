FROM alpine

MAINTAINER packeteer <packeteer@gmail.com>

RUN apk add --no-cache nginx

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
