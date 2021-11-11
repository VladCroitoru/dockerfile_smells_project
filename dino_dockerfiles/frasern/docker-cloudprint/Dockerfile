FROM ubuntu:16.04

RUN apt-get update \
  && apt-get install -y cloudprint \
  && apt-get clean \ 
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/
