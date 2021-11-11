FROM golang@sha256:2ffa2f093d20c46e86435626f11bf163797400cf8f7cf14ecdc6403f1930045c

COPY *.go Gopkg.* /go/src/key-forge/

RUN set -x \
 && go get -u github.com/golang/dep/cmd/dep \
 && cd /go/src/key-forge \
 && dep ensure \
 && GOOS=linux GOARCH=amd64 go build . \
 && GOOS=windows GOARCH=amd64 go build . \
 && sha256sum key-forge* > sha256sum.txt \
 && cat sha256sum.txt

FROM debian:stretch

COPY --from=0 /go/src/key-forge/key-forge* /go/src/key-forge/sha256sum.txt /usr/local/bin/

ENTRYPOINT [ "key-forge" ]
