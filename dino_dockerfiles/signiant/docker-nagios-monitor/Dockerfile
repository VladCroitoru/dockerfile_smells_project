FROM alpine:3.7

RUN apk add --no-cache ca-certificates curl

ADD start.sh /
RUN chmod 777 /start.sh

CMD ["sh", "/start.sh"]
