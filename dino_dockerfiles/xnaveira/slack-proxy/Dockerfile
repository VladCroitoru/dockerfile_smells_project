FROM golang:latest
ENV appdir /go/src/github.com/xnaveira/slack-proxy
RUN wget -q https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 -O /usr/local/bin/dep
RUN chmod +x /usr/local/bin/dep
RUN mkdir -p ${appdir}
COPY . ${appdir}
WORKDIR ${appdir}
RUN dep ensure
RUN go build -o main .
EXPOSE 8080
CMD ["/go/src/github.com/xnaveira/slack-proxy/main"]
