FROM alpine:3.3

RUN apk update && apk add nodejs unzip wget && rm -rf /var/cache/apk/*

ADD launch.sh /launch.sh
RUN chmod 755 /launch.sh

CMD ["ash", "/launch.sh"]
