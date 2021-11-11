FROM golang:1.8.1

# system dependencies
RUN apt-get update && apt-get -y install bzr build-essential curl git mercurial pkg-config

# install docker
RUN apt-get install -y --no-install-recommends apt-transport-https ca-certificates software-properties-common
RUN curl -fsSL https://apt.dockerproject.org/gpg | apt-key add -
RUN add-apt-repository "deb https://apt.dockerproject.org/repo/ debian-$(lsb_release -cs) main"
RUN apt-get update && apt-get -y --no-install-recommends install docker-engine

# common utilities
RUN go get github.com/convox/rerun
RUN go get github.com/kardianos/govendor
