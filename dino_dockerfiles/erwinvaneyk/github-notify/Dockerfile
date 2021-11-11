FROM ubuntu
MAINTAINER Erwin van Eyk <erwinvaneyk@gmail.com>

# Install dependencies
RUN apt-get update && apt-get install golang git -y

# Build application
ENV GOPATH /go/
ADD . $GOPATH/src/github-notify/
WORKDIR $GOPATH/src/github-notify/
RUN go get
RUN go build -o /bin/github-notify

# Program default variables
ENV CHECK_INTERVAL 300

ENTRYPOINT ["github-notify"]