FROM golang:1.8
COPY . "$GOPATH/src/github.com/Mensu/Agenda-cli-service-Go"
RUN cd "$GOPATH/src/github.com/Mensu/Agenda-cli-service-Go/cli" && go get -v && go install -v
RUN cd "$GOPATH/src/github.com/Mensu/Agenda-cli-service-Go/service" && go get -v && go install -v
WORKDIR /
EXPOSE 8080
VOLUME ["/data"]
