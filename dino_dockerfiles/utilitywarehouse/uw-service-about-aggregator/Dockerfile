FROM alpine:3.4

ADD *.go /uw-service-about-aggregator/
ADD *.html /

RUN apk add --no-cache ca-certificates \
  && apk add --update bash \
  && apk --update add git bzr \
  && apk --update add go \
  && export GOPATH=/gopath \
  && REPO_PATH="github.com/utilitywarehouse/uw-service-about-aggregator" \
  && mkdir -p $GOPATH/src/${REPO_PATH} \
  && mv uw-service-about-aggregator/* $GOPATH/src/${REPO_PATH} \
  && rm -rf uw-service-about-aggregator \
  && cd $GOPATH/src/${REPO_PATH} \
  && go get -t ./... \
  && go build \
  && mv uw-service-about-aggregator /uw-service-about-aggregator \
  && apk del go git bzr \
  && rm -rf $GOPATH /var/cache/apk/*

CMD [ "/uw-service-about-aggregator" ]