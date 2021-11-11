FROM golang:latest
MAINTAINER paulcull <dev@pkhome.co.uk>

RUN apt-get -qy update && apt-get -qy install vim-common gcc mercurial supervisor

ADD        . /go/src/github.com/paulcull/go-webbrick
WORKDIR    /go/src/github.com/paulcull/go-webbrick/mqtt_webbrick
RUN 	   rm mqtt_webbrick

RUN  go get -v
RUN  go build -ldflags " \
       -X main.buildVersion=$(grep "const Version " ../version.ver | sed -E 's/.*"(.+)"$/\1/' ) \
       -X main.buildRevision=$(git rev-parse --short HEAD) \
       -X main.buildBranch=$(git rev-parse --abbrev-ref HEAD) \
       -X main.buildDate=$(date +%Y%m%d-%H:%M:%S) \
       -X main.goVersion=$GOLANG_VERSION \
     "


ADD etc/supervisor.conf /etc/supervisor/conf.d/go-webbrick.conf
  
EXPOSE 9001 1883
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/go-webbrick.conf
