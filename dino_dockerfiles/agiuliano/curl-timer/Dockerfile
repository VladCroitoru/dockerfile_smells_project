FROM alpine

RUN apk add --update bash curl && rm -rf /var/cache/apk/*

COPY timer.sh /timer.sh
RUN chmod +x /timer.sh

CMD ["/bin/bash", "/timer.sh"]
