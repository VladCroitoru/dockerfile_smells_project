FROM golang:latest

MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>

WORKDIR /go/src/app
COPY . .

RUN go-wrapper download
RUN CGO_ENABLED=0 GOOS=linux go build -a -o dbrpc

FROM scratch

WORKDIR /
COPY --from=0 /go/src/app/dbrpc .

EXPOSE 8080
ENTRYPOINT ["/dbrpc"]
