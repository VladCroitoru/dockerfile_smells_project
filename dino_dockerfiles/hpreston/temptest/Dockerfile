FROM debian:latest
MAINTAINER Hank Preston <hapresto@cisco.com>

RUN apt-get update \
 && rm -rf /var/lib/apt/lists/*
 
EXPOSE 80 

COPY hello_world.sh /root/
RUN chmod +x /root/hello_world.sh

CMD ["/root/hello_world.sh"]
