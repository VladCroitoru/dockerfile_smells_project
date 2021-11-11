FROM ubuntu:16.04
MAINTAINER hg8496@cstolz.de

ADD own-volume.sh /usr/local/bin/own-volume
ADD setup_server_xml.sh /usr/local/bin/setup_server_xml.sh
ADD db_extract.sh /usr/local/bin/db_extract.sh

RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install sudo software-properties-common software-properties-common xmlstarlet curl -y \
  && echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
  && apt-add-repository ppa:webupd8team/java -y \
  && apt-get update \
  && apt-get install oracle-java8-installer -y \
  && /usr/sbin/groupadd atlassian \
  && /usr/sbin/useradd --create-home --home-dir /opt/atlassian -g atlassian --shell /bin/bash atlassian \
  && mkdir -p /opt/atlassian-home \
  && chown -R atlassian:atlassian /opt/atlassian-home \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && echo "%atlassian ALL=NOPASSWD: /usr/local/bin/own-volume" >> /etc/sudoers

ENV CONTEXT_PATH ROOT

