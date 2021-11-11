FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
# a bit modified Aaron Darling's Dockerfile, Procfile and run files

RUN apt-get update -y && \
    apt-get install -y openjdk-8-jre-headless

ADD http://downloads.sourceforge.net/project/ngopt/a5_miseq_linux_20150522.tar.gz /a5_miseq.tar.gz

RUN mkdir /a5_miseq
RUN tar xzf /a5_miseq.tar.gz --directory /a5_miseq --strip-components=1


ADD run /usr/local/bin/
ADD Procfile /
ENTRYPOINT ["run"]
