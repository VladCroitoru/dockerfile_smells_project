FROM debian:jessie
MAINTAINER willou.com@gmail.com

# install socat
RUN apt-get update \
  && apt-get install -y socat \
  && rm -rf /var/lib/apt/lists/*

# docker tcp port
EXPOSE 2375

ENTRYPOINT ["socat", "TCP-LISTEN:2375,reuseaddr,fork","UNIX-CLIENT:/var/run/docker.sock"]
