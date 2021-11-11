FROM golang:1.17.1-buster AS builder

WORKDIR $GOPATH/src/cdbot
COPY go.mod .
RUN GOPROXY="https://goproxy.cn" GO111MODULE=on go mod download -x
COPY . .
RUN CGO_ENABLED=0 go build -o /opt/main ./src/main.go

FROM debian:10
RUN sed -i -r 's/(deb|security).debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    apt update && apt install -y ca-certificates && rm -r /var/lib/apt/lists
COPY --from=builder /opt/main /opt/main
EXPOSE 8080
CMD ["/opt/main"]
