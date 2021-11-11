# VERSION 1.1.0

FROM keboola/base
MAINTAINER Tomáš Mudruňka <mudrunka@geneea.com>

# setup the environment
WORKDIR /tmp
RUN yum -y install wget git
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install requests
RUN pip install PyYaml

# prepare the container
WORKDIR /home
COPY src src/

ENTRYPOINT python ./src/topic.py --data=/data
