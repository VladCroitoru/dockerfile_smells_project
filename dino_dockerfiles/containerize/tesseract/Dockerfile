FROM golang:alpine

RUN set -ex && \
    apk add --update --no-cache ca-certificates openssl imagemagick && \
    echo 'http://dl-4.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories && \
    apk add --update --no-cache tesseract-ocr && \
    wget -q -P /usr/share/tessdata/ https://github.com/tesseract-ocr/tessdata/raw/master/chi_tra.traineddata && \
    wget -q -P /usr/share/tessdata/ https://github.com/tesseract-ocr/tessdata/raw/master/por.traineddata