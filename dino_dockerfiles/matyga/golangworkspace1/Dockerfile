FROM golang:1.9.2-alpine

ADD . /go/src/github.com/matyga/GolangWorkspace1
RUN go install github.com/matyga/GolangWorkspace1

WORKDIR /go/src/github.com/matyga/GolangWorkspace1

EXPOSE 8080

ENTRYPOINT ["go","run","main.go"] 

