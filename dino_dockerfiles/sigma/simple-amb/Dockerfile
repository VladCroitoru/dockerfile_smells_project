FROM debian:latest
MAINTAINER Yann Hodique <hodiquey@vmware.com>
ENV REFRESHED_AT 12/2/2014

RUN apt-get update
RUN apt-get install -y socat

ADD forward.sh /usr/local/bin/forward.sh

# clean any temp files
RUN apt-get autoclean
RUN apt-get autoremove
RUN apt-get clean
RUN rm -rf /tmp/*

EXPOSE 10000

ENTRYPOINT ["/usr/local/bin/forward.sh"]
