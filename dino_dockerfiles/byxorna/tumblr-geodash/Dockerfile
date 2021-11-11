FROM golang
MAINTAINER Gabe Conradi <gummybearx@gmail.com>
ADD . /go/src/github.com/byxorna/tumblr-geodash
RUN apt-get update && apt-get install -y libgeoip-dev pkg-config && rm -rf /var/lib/apt/lists/*
RUN go get github.com/tools/godep && cd /go/src/github.com/byxorna/tumblr-geodash && ./install.sh
ADD ./public/ /srv/www
WORKDIR /srv/www
EXPOSE 8080
CMD ["server"]

