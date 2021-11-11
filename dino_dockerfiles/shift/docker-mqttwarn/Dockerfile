FROM ubuntu:14.10
MAINTAINER Vincent Palmer <shift+gh@someone.section.me>

RUN apt-get update \
    && apt-get upgrade --yes --force-yes \
    && apt-get install wget git-core python python-pip --yes --force-yes \
    && pip install paho-mqtt \
    && git clone https://github.com/jpmens/mqttwarn.git

ADD run.sh /run.sh
RUN chmod u+x /run.sh
ENTRYPOINT /run.sh
