FROM ubuntu:wily

MAINTAINER Marek Kolodziej

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install ruby rubygems

RUN gem install fakes3

RUN mkdir -p /tmp/fakes3_root

CMD ["/usr/local/bin/fakes3", "-r", "/tmp/fakes3_root", "-p", "4567"]

