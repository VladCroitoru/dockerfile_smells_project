FROM ubuntu:14.04
MAINTAINER Yasser Nabi "yassersaleemi@gmail.com"
ENV DEBIAN_FRONTEND noninteractive

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \
        apt-get update && \
        apt-get -y install \
            python \
            python-requests

ADD ./dnsimple_update.py /dnsimple_update.py

ENTRYPOINT ["/usr/bin/python", "/dnsimple_update.py"]
