FROM gliderlabs/alpine

RUN apk add --update bash curl ca-certificates && rm -rf /var/cache/apk/*

ADD wrapper.sh /
ADD calculate.sh /
CMD ["/wrapper.sh"]
