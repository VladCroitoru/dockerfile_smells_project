# FROM phusion/baseimage:latest
FROM debian:jessie-slim

WORKDIR /usr/src

RUN \
  apt-get update \
  && apt-get -y install tcl8.6 tk8.6 tcllib libsqlite3-tcl libtk-img wget unzip \
  && mkdir -p /usr/src 

RUN \
  wget "https://downloads.sourceforge.net/project/drakon-editor/drakon_editor1.27.zip?r=http%3A%2F%2Fdrakon-editor.sourceforge.net%2Feditor.html&ts=$(date +%s)&use_mirror=superb-dca2" -O drakon_editor1.27.zip \
  && unzip drakon_editor1.27.zip
  

CMD ["/usr/src/drakon_editor.tcl"]
