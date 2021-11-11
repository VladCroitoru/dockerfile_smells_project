FROM ubuntu:16.04

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y lm-sensors && \
  mkdir -p /home/node-exporter \
  mkdir -p /home/share

COPY script.sh /home/

CMD ["/home/script.sh"]
