FROM alpine

RUN apk add --no-cache inotify-tools bash gawk sed grep bc coreutils jq
RUN apk add --update curl

ADD entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]




