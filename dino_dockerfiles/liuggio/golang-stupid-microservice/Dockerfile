
FROM google/golang:stable
# Godep for vendoring
RUN go get github.com/tools/godep
RUN go get gopkg.in/mgo.v2
# Recompile the standard library without CGO
RUN CGO_ENABLED=0 go install -a std

MAINTAINER liuggio@gmail.com
ENV APP_DIR $GOPATH/src/github.com/golangit/golang-stupid-microservice
 
# Set the entrypoint 
ENTRYPOINT ["/opt/app/golang-stupid-microservice"]
ADD . $APP_DIR

# Compile the binary and statically link
RUN mkdir /opt/app
# RUN cd $APP_DIR
RUN cd $APP_DIR && CGO_ENABLED=0 go build -o /opt/app/golang-stupid-microservice -ldflags '-d -w -s'

EXPOSE 80
