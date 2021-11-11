FROM ubuntu:latest
MAINTAINER Michael Choi <mjchoi45@gmail.com>

RUN apt-get update -q
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy ca-certificates stunnel4 --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN sed -i 's/^ENABLED=0/ENABLED=1/' /etc/default/stunnel4

ADD https://gist.githubusercontent.com/mjchoi/2da6c9c4a5e9356cac74/raw/be022f804ec00e2dd4fd1278724786b25fe02c7d/found-us-east-1.conf /etc/stunnel/found-us-east-1.conf

EXPOSE 19200
CMD ["service", "stunnel4", "start"]
