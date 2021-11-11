FROM google/cloud-sdk

RUN apt-get update && apt-get -y install git && mkdir /go

ENV PATH $PATH:/usr/local/go_appengine:/usr/local/go/bin:/go/bin
ENV GOPATH /go
ENV GAE_SDK_GO_VER 1.9.36
ENV GAE_SDK_GO_ZIP go_appengine_sdk_linux_amd64-$GAE_SDK_GO_VER.zip
ENV GO_VER 1.5.4
ENV GO_GZ go$GO_VER.linux-amd64.tar.gz

ADD https://storage.googleapis.com/appengine-sdks/featured/$GAE_SDK_GO_ZIP .
RUN unzip -q $GAE_SDK_GO_ZIP -d /usr/local && rm -f $GAE_SDK_GO_ZIP

ADD https://storage.googleapis.com/golang/$GO_GZ .
RUN tar -C /usr/local -xzf $GO_GZ && rm -f $GO_GZ

RUN go get github.com/tools/godep
