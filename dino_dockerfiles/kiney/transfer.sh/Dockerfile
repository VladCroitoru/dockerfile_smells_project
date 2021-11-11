FROM golang
MAINTAINER Jannik Winkel <jannik.winkel@kiney.de>

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

# Copy the local package files to the container's workspace.
ADD ./transfersh-server /go/src/app

# install dependencies
RUN go get ./

# build & install server
RUN go install . 

RUN mkdir /data

ENTRYPOINT ["/go/bin/app", "--port", "8080"]  
CMD ["--provider", "local", "--basedir", "/srv/"]

VOLUME ["/data"]

#TODO: why expose 6060??
EXPOSE 8080 6060
