
FROM golang:1.10

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y zip

RUN curl https://glide.sh/get | sh

RUN cd $GOPATH

RUN mkdir /dist

ENV PROJECT_ROOT=$GOPATH/src/github.com/watermint/dcfg
RUN mkdir -p $PROJECT_ROOT

ADD . $PROJECT_ROOT
ENTRYPOINT $PROJECT_ROOT/build/build_inside_docker.sh

