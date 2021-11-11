FROM golang:1.6
RUN go get github.com/rancher/trash
RUN go get github.com/golang/lint/golint
RUN curl -sL https://get.docker.com/builds/Linux/x86_64/docker-1.9.1 > /usr/bin/docker && \
    chmod +x /usr/bin/docker
RUN apt-get update && \
    apt-get install -y xz-utils
