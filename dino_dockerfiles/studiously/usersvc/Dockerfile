FROM golang:alpine

RUN apk add --no-cache git
RUN go get github.com/Masterminds/glide
WORKDIR /go/src/github.com/studiously/usersvc

ADD ./glide.yaml ./glide.yaml
ADD ./glide.lock ./glide.lock
RUN glide install --skip-test -v
ADD . .
RUN GOOS=linux GOARCH=amd64 go build -o usersvc_linux-amd64

FROM scratch

WORKDIR /
COPY --from=0 /go/src/github.com/studiously/usersvc/usersvc_linux-amd64 ./usersvc

ENTRYPOINT usersvc host