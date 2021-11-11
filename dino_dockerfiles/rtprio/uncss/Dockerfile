FROM centos:latest
MAINTAINER Elliot Schlegelmilch <elliot@schlegelmilch.org>

RUN yum install -y wget epel-release bzip2 && yum install -y npm fontconfig
RUN mkdir -p /usr/local/bin

RUN cd /tmp; wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
   bunzip2 phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
   tar -x -f phantomjs-2.1.1-linux-x86_64.tar; mv  phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/ && rm -Rf /tmp/phantom*

RUN npm install -g uncss

CMD [ "/bin/sh" ]
