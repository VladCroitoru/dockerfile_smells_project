FROM alpine

MAINTAINER Knut Ahlers <knut@luzifer.io>
EXPOSE 3000
ENV GOPATH /go

RUN apk --update add go gnupg git

ADD . /go/src/github.com/Luzifer/gpg_verify
WORKDIR /go/src/github.com/Luzifer/gpg_verify
RUN go get github.com/tools/godep \
 && /go/bin/godep go build \
 && apk --purge del go git

ENTRYPOINT ["/go/src/github.com/Luzifer/gpg_verify/gpg_verify"]
CMD ["--"]
