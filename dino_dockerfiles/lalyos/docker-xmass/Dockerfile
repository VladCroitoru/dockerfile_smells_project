FROM alpine:3.4

RUN apk add -U curl
RUN apk add nginx
RUN apk add bash

RUN mkdir /run/nginx
ENV BODY welcome
ENV BGCOLOR lightgreen
ENV TITLE meri kriszmasz

COPY ./start /
CMD /start
