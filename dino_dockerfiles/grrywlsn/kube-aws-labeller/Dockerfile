FROM alpine:3.5

ENV GOPATH=/go

WORKDIR /go/src/app
ADD . /go/src/app/
ADD https://storage.googleapis.com/kubernetes-release/release/v1.6.1/bin/linux/amd64/kubectl /usr/local/bin/kubectl

RUN apk --no-cache add ca-certificates git go musl-dev \
  && chmod +x /usr/local/bin/kubectl \
  && go get ./... \
  && CGO_ENABLED=0 go build -ldflags '-s -extldflags "-static"' -o /kube-aws-labeller . \
  && apk del go git musl-dev \
  && rm -rf $GOPATH

CMD [ "/kube-aws-labeller" ]
