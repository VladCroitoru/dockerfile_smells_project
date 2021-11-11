FROM golang:1.4.2

ADD . /go/src/cerebro
WORKDIR /go/src/cerebro
RUN go get
RUN go install

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/go/bin/cerebro"]
EXPOSE 8080
