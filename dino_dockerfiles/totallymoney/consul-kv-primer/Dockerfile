FROM alpine:latest
RUN apk add --update bash curl && rm -rf /var/cache/apk/*
COPY prime.sh /prime.sh
CMD /prime.sh
