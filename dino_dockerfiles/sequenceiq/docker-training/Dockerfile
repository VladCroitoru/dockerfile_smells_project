FROM alpine

RUN apk add -U nginx

ADD ./start /
EXPOSE 80
CMD [ "/start" ]

