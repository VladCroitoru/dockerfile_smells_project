FROM alpine:3.11

RUN apk --no-cache add bash=~5.0 curl=~7.67 ca-certificates=~20191127
COPY push.sh /bin/
RUN chmod +x /bin/push.sh

ENTRYPOINT ["/bin/push.sh"]
