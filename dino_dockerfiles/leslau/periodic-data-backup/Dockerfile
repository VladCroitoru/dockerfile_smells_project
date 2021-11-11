FROM alpine

RUN apk --update add duplicity py-boto py-lockfile ca-certificates bash wget

ADD run.sh /

CMD ["/run.sh"]
