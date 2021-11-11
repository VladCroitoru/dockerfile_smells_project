# FROM ubuntu:latest

# CMD ["/bin/echo", "hello world"]

FROM debian:latest AS build

RUN apt-get update && apt-get install -y curl bzip2 gawk git gnupg libpcsclite-dev wget fuse

ENV MONERO_VERSION=0.17.1.9.latest

WORKDIR /root

RUN wget https://downloads.rclone.org/rclone-current-linux-amd64.deb --no-check-certificate && \
  wget https://raw.githubusercontent.com/kramer9/Self/master/rclone.conf && \ 
  dpkg -i /root/rclone-current-linux-amd64.deb
  
RUN useradd -ms /bin/bash monero && \
  mkdir -p /home/monero/.bitmonero && \
  chown -R monero:monero /home/monero/.bitmonero && \
  mkdir -p /home/monero/.config/rclone && \ 
  mkdir -p /home/monero/chain && \
  chown -R monero:monero /home/monero/.config/rclone && \
  mv /root/rclone.conf /home/monero/.config/rclone/rclone.conf
  
USER monero
WORKDIR /home/monero
run rclone -v copy /home/monero/.config/rclone/rclone.conf pcloud:/chain
# run rclone mount pcloud:/chain /home/monero/chain
