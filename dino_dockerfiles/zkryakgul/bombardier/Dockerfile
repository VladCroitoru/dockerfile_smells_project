FROM golang:jessie
MAINTAINER Zekeriya Akgül


RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y iputils-ping iproute2 net-tools wget ethtool

RUN go get -u github.com/codesenberg/bombardier


EXPOSE 80 443 444

ENTRYPOINT ["/bin/bash"]
