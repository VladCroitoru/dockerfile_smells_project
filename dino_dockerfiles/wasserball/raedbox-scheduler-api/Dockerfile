FROM golang:latest
USER root

# update
RUN apt-get update

# install vim
RUN apt-get install -y vim

# Add workers
ADD main.go /go/src/github.com/wasserball/raedbox/scheduler-api/
# install dependencies
RUN go get "github.com/PuerkitoBio/goquery"

# create config dir
RUN mkdir -p /data
RUN chmod 777 /data
ADD ./data  /data

# install api
RUN go install github.com/wasserball/raedbox/scheduler-api


# Set the timezone.
RUN echo "Europe/Vienna" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

ENTRYPOINT /go/bin/scheduler-api

EXPOSE 8081