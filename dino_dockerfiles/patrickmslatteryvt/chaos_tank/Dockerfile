FROM golang:1.10

RUN git clone https://github.com/vncntvandriessche/chaos_tank.git /go/src/chaos_tank
WORKDIR /go/src/chaos_tank
RUN go get -d -v ./...

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
