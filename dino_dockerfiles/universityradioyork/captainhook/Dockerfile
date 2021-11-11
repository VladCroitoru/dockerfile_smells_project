FROM gliderlabs/alpine:3.1

ENTRYPOINT ["/opt/captainhook"]

COPY . /go/src/github.com/UniversityRadioYork/captainhook
RUN apk-install -t build-deps go git mercurial \
    && cd /go/src/github.com/UniversityRadioYork/captainhook \
    && export GOPATH=/go \
    && go get \
    && go build -o /opt/captainhook \
    && rm -rf /go \
    && apk del --purge build-deps

EXPOSE 4665