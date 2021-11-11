FROM debian:jessie
MAINTAINER Pierre Cheynier <pierre.cheynier@sfr.com>

RUN apt-get update && \
    apt-get install -y ansible python-pip software-properties-common openssh-client && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/cache/apt /var/lib/apt/lists

WORKDIR /etc/ansible
RUN echo '[local]\nlocalhost\n' > hosts
RUN pip install docker-py==1.1.0
