FROM golang
 
ADD .  ~/Desktop/learning_docker
RUN mkdir /go/src/learning_docker
COPY main.go  /go/src/learning_docker
RUN go install learning_docker
ENTRYPOINT ["/go/bin/learning_docker"]

EXPOSE 8080