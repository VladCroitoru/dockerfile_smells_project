FROM debian:jessie
MAINTAINER Anthony Dahanne <anthony.dahanne@gmail.com>

RUN apt-get update \ 
  && apt-get install -y socat \
  && rm -rf /var/lib/apt/lists/*

VOLUME /var/run/docker.sock

# docker tcp port
EXPOSE 2375

ENTRYPOINT ["socat", "TCP-LISTEN:2375,reuseaddr,fork","UNIX-CLIENT:/var/run/docker.sock"]
