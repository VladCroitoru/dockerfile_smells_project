FROM ubuntu:latest
MAINTAINER Alan Scherger <flyinprogrammer@gmail.com>

RUN apt-get install -y whois && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

ENTRYPOINT ["/usr/bin/mkpasswd"]
CMD ["-m", "sha-512"]