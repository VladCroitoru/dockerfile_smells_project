FROM golang as build

COPY . /go/src/github.com/DiamondYuan/image-cleaner

ENV CGO_ENABLED=0

RUN curl https://glide.sh/get | sh

RUN cd /go/src/github.com/DiamondYuan/image-cleaner && \
    glide install && \
    go test && \
	go build

FROM alpine

COPY --from=build /go/src/github.com/DiamondYuan/image-cleaner/image-cleaner /usr/bin/

WORKDIR /

ENTRYPOINT ["image-cleaner"]

CMD ["-dryRun"]