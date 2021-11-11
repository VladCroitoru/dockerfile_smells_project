FROM google/golang

WORKDIR /gopath/src/app
ADD . /gopath/src/app/
RUN go get github.com/Sirupsen/logrus
RUN go get github.com/hashicorp/consul/api
RUN go build -o conductor && mkdir /gopath/bin && cp conductor /gopath/bin/conductor

CMD ["--consul", "consul:8500"]
ENTRYPOINT ["/gopath/bin/conductor"]
