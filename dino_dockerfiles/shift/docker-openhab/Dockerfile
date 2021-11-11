FROM ubuntu:14.10
MAINTAINER Vincent Palmer <shift+gh@someone.section.me>

RUN apt-get update \
    && apt-get upgrade --yes --force-yes \
    && apt-get install wget git-core unzip python python-bs4 --yes --force-yes \
    && wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /tmp/jdk-7u67-linux-x64.tar.gz http://download.oracle.com/otn-pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.tar.gz \
    && tar -zxC /opt -f /tmp/jdk-7u67-linux-x64.tar.gz \
    && ln -s /opt/jdk1.7.0_67 /opt/jdk7 \
    && rm -rf /tmp/jdk-7u67-linux-x64.tar.gz \
    && mkdir -p /srv/openhab/tmp /srv/openhab/runtime /srv/openhab/addons /srv/openhab/addons-available \
    && wget -O /srv/openhab/tmp/runtime.zip https://github.com/openhab/openhab/releases/download/v1.6.2/distribution-1.6.2-runtime.zip \
    && wget -O /srv/openhab/tmp/addons.zip https://github.com/openhab/openhab/releases/download/v1.6.2/distribution-1.6.2-addons.zip \
    && cd /srv/openhab/runtime \
    && unzip /srv/openhab/tmp/runtime.zip \
    && rm /srv/openhab/tmp/runtime.zip \
    && cd /srv/openhab/addons-available \
    && unzip /srv/openhab/tmp/addons.zip \
    && rm /srv/openhab/tmp/addons.zip \
    && cd /srv/openhab/addons-available \
    && wget https://my.openhab.org/downloads/org.openhab.io.myopenhab-1.4.0-SNAPSHOT.jar
ADD run.sh /run.sh
RUN chmod u+x /run.sh
ENTRYPOINT /run.sh
