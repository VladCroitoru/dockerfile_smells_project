FROM alpine:3.7

RUN apk --no-cache add busybox-extras tcpdump curl

COPY kluster_sanity.sh /
CMD ["/kluster_sanity.sh"]
