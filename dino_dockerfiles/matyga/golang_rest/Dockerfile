FROM golang

ADD . /go/src/github.com/matyga/golang_rest
RUN go get github.com/gorilla/mux
RUN go install github.com/matyga/golang_rest
WORKDIR /go/src/github.com/matyga/golang_rest



EXPOSE 8080

ENTRYPOINT ["go","run","rest1.go"] 

