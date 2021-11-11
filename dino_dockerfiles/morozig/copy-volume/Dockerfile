FROM alpine

RUN apk --no-cache add rsync

CMD ["rsync", "-a", "--delete", "/from/", "/to"]
