FROM alpine:3.9

LABEL maintainer="beudbeud@beudibox.fr"

RUN apk update && apk add build-base python3 python3-dev graphicsmagick ffmpeg zlib-dev jpeg-dev

RUN pip3 install prosopopee==1.1.4

RUN mkdir /site

WORKDIR /site

ENTRYPOINT ["prosopopee"]

EXPOSE 9000
