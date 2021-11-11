FROM golang:1.8
COPY . "$GOPATH/src/github.com/Suenaa/agenda-golang"
RUN cd "$GOPATH/src/github.com/Suenaa/agenda-golang/cli" && go get -v && go install -v
RUN cd "$GOPATH/src/github.com/Suenaa/agenda-golang/service" && go get -v && go install -v
WORKDIR /
EXPOSE 8080
VOLUME [ "/data" ]
