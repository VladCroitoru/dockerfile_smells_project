FROM golang:alpine
LABEL mantainer="t@avelino.xxx"

RUN apk --no-cache add git wget
WORKDIR /go/src/github.com/structy/structbase
COPY . /go/src/github.com/structy/structbase

# Go dep!
RUN go get -u github.com/golang/dep/... && \
    dep ensure && \
    go install && \
    wget https://raw.githubusercontent.com/nuveo/tcp-port-wait/master/tcp-port-wait.sh && \
    chmod +x tcp-port-wait.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]
CMD ["structbase"]
