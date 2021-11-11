FROM golang

MAINTAINER Nicole Nie <nieyuanyuan@huawei.com>

VOLUME /opt

RUN apt-get update && apt-get install -y wget git make ; \
		cd /opt ; \
		export PATH=$GOROOT/bin:$GOPATH/bin:$PATH ; \
		go get -d github.com/nieyy/test ; \
		cd $GOPATH/src/github.com/nieyy/test ; \
		go build ; cp test /usr/bin/

EXPOSE 8000

CMD ["/usr/bin/test"]