FROM alpine:3.6

RUN apk update && apk add perl perl-dev curl build-base && \
    apk add --no-cache wget && \
    curl -L https://cpanmin.us | perl - App::cpanminus && \
    cpanm Reply

CMD ["reply"]
