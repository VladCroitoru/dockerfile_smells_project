# Start with golang base image ye
FROM golang:latest
MAINTAINER Omar Qazi (omar@smick.co)

# Compile latest source
COPY . /go/src/github.com/omarqazi/hearst
RUN go get github.com/omarqazi/hearst
RUN go get bitbucket.org/liamstask/goose/cmd/goose
RUN go install github.com/omarqazi/hearst

WORKDIR /go/src/github.com/omarqazi/hearst
CMD /go/bin/hearst
EXPOSE 8080
