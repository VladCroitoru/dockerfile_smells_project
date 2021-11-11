FROM alpine

RUN apk --update add ympd && \
    rm -rf /var/cache/apk/*

EXPOSE 8080

CMD ["ympd", "-h","mpdhost"]
