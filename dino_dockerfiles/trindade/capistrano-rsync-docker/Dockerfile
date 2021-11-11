FROM debian:jessie

MAINTAINER Pedro Trindade <trindade.pedro@ubbin.com>

RUN apt-get update && apt-get install -y rubygems git curl
RUN gem install net-ssh -v 4.0.1
RUN gem install capistrano -v 3.7.1
RUN gem install capistrano-rsync

WORKDIR /root/workdir

ENTRYPOINT ["cap"]
