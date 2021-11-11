FROM debian:jessie
RUN DEBIAN_FRONTENT=noninteractive && \
  apt-get update && apt-get -y install jq curl

COPY bin/ /opt/resource/
RUN chmod +x /opt/resource/*
