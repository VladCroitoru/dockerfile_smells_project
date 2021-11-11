FROM alpine:3.4

RUN apk update && apk add rsync
ADD sync.sh /sync.sh
RUN chmod +x /sync.sh

CMD ["/sync.sh"]
