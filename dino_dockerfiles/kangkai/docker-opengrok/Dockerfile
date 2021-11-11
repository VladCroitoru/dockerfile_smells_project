FROM ubuntu:14.04
MAINTAINER Zero Cho "http://itsze.ro/"

ENV OPENGROK_INSTANCE_BASE /grok

RUN apt-get update
RUN apt-get install -y openjdk-7-jre-headless exuberant-ctags git subversion mercurial tomcat7 wget inotify-tools
RUN locale-gen en_US.UTF-8
ADD install.sh /usr/local/bin/install
RUN /usr/local/bin/install
ADD run.sh /usr/local/bin/run
ENTRYPOINT ["/usr/local/bin/run"]

EXPOSE 8080
