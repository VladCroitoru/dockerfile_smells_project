FROM        google/golang
MAINTAINER  SideCar6, Jack Brown & Matt Merkes

RUN         mkdir -p /gopath/src/aegis
WORKDIR     /gopath/src/aegis
EXPOSE      3000
ENTRYPOINT  ["go"]
CMD         ["run", "server.go"]

ADD         . /gopath/src/aegis/.
RUN         go get
