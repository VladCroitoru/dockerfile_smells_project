FROM alpine

WORKDIR /srv

RUN apk --no-cache add --virtual .builddeps ca-certificates curl wget tar gzip && \
    wget $(curl -sL https://api.github.com/repos/spf13/hugo/releases/latest | grep 'Linux-64bit.tar.gz' | grep 'browser_download_url' | cut -d '"' -f 4) && \
    tar -zxvf hugo_*_Linux-64bit.tar.gz && \
    apk del .builddeps && \
    mv hugo /usr/local/bin/ && \
    rm -rf /srv/*

ENTRYPOINT ["hugo"]

CMD ["help"]

