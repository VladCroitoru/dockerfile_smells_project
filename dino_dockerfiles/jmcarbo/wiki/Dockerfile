FROM google/golang:stable

MAINTAINER Yuji ODA

RUN go get github.com/revel/cmd/revel

ADD . /gopath/src/github.com/jmcarbo/wiki
RUN revel build github.com/jmcarbo/wiki /usr/local/wiki

ENV DB_DRIVER sqlite3
ENV DB_SOURCE ./wiki.db

EXPOSE 9000

WORKDIR /usr/local/wiki
CMD []
ENTRYPOINT ["./run.sh"]
