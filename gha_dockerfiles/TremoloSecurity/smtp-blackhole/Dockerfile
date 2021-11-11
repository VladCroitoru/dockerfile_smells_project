FROM ubuntu:18.04

MAINTAINER Tremolo Security, Inc. - Docker <docker@tremolosecurity.com>


LABEL io.k8s.description="Blackhole" \
      io.k8s.display-name="Blackhole" 

RUN apt-get update;apt-get -y install python3 python3-pip && \
    apt-get -y upgrade;apt-get clean;rm -rf /var/lib/apt/lists/*; \
    groupadd -r blackhole -g 433 && \
    mkdir /usr/local/blackhole && \
    useradd -u 431 -r -g blackhole -d /usr/local/blackhole -s /sbin/nologin -c "Blackhole image user" blackhole && \
    pip3 install blackhole

ADD bh-config.txt /usr/local/blackhole/bh-config.txt



USER 431

CMD ["blackhole","-c","/usr/local/blackhole/bh-config.txt","-d"]