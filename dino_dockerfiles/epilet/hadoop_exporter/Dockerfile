FROM golang:1.8

WORKDIR /go/src/app
COPY . .
RUN curl https://glide.sh/get | sh && \
    glide i && \
    go build
ENTRYPOINT ["/go/src/app/app"]
