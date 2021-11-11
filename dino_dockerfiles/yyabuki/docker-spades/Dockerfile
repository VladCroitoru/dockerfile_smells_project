FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
# We modified Dockerfile and attached files created by Michael Barton.

RUN apt-get update -y
RUN apt-get install -y python

ADD http://spades.bioinf.spbau.ru/release3.1.0/SPAdes-3.1.0-Linux.tar.gz /tmp/
RUN tar xzf /tmp/SPAdes-3.1.0-Linux.tar.gz
WORKDIR /SPAdes-3.1.0-Linux
RUN mv bin/* /usr/local/bin/
RUN mv share/* /usr/local/share/

ADD run /usr/local/bin/
ADD Procfile /
WORKDIR /

ENTRYPOINT ["/usr/local/bin/run"]
