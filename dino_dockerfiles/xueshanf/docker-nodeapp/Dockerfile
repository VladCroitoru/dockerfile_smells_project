#FROM dockerfile/nodejs:latest
FROM gliderlabs/alpine:latest

ENV DEBIAN_FRONTEND noninteractive
RUN apk --update add wget nodejs

#RUN apt-get update && apt-get install -y curl wget nodejs

ADD ./demo /demo

#RUN ln -s /usr/bin/nodejs /usr/bin/node

VOLUME /demo

EXPOSE 8000
CMD    ["/demo/bin/www"]
