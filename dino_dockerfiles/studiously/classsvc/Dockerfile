FROM golang:alpine AS build-env

RUN apk add --no-cache git
RUN go get github.com/Masterminds/glide
WORKDIR /go/src/github.com/studiously/classsvc

ADD ./glide.yaml ./glide.yaml
ADD ./glide.lock ./glide.lock
RUN glide install --skip-test -v
ADD . .
RUN GOOS=linux GOARCH=amd64 go build -o classsvc_linux-amd64

FROM scratch
WORKDIR /
COPY --from=build-env /go/src/github.com/studiously/classsvc/classsvc_linux-amd64 ./classsvc
ENTRYPOINT classsvc host
EXPOSE 8080 8081