FROM ubuntu:14.04.2
MAINTAINER ming <qm2009@gmail.com>

RUN apt-get update && \
    apt-get install -y python-pip python-m2crypto openssh-server
RUN pip install shadowsocks==2.6.10


# Configure container to run as an executable
ENTRYPOINT ["/usr/local/bin/sslocal"]
