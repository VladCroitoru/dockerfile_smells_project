FROM  fedora:21

MAINTAINER fabric8.io <fabric8@googlegroups.com>

RUN yum install -y git

RUN useradd fabric8

WORKDIR /home/fabric8

ADD start.sh ./

RUN chown -R fabric8:fabric8 /home/fabric8

USER fabric8

CMD /home/fabric8/start.sh