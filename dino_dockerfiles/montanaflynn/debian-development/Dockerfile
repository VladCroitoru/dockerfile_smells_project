FROM debian:jessie
MAINTAINER Montana Flynn <montana@montanaflynn.me>

RUN apt-get update && \
    apt-get install -y sudo curl wget nano vim git telnet siege jq && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/bin/bash"]
