FROM alpine:3.7

RUN apk add --update --no-cache lvm2 e2fsprogs jq

COPY execute.sh /

RUN chmod +x /

CMD ["/execute.sh"]
