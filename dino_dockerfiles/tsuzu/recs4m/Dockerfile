FROM golang:1.12 as build

RUN go get github.com/cs3238-tsuzu/recs4m

FROM tsuzu/gmusic

COPY --from=build /go/bin/recs4m /bin/
COPY ./html /
COPY ./upload.sh /root

RUN apt-get install -y language-pack-ja && \
    chmod +x /root/upload.sh

EXPOSE 80
WORKDIR /
CMD ["recs4m", "--upload-script", "/root/upload.sh"]
