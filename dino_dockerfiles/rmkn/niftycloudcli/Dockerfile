FROM centos:6
MAINTAINER rmkn
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8 && sed -i -e "s/en_US.UTF-8/ja_JP.UTF-8/" /etc/sysconfig/i18n
RUN cp -p /usr/share/zoneinfo/Japan /etc/localtime && echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock
RUN yum -y update
RUN yum -y install java-1.8.0-openjdk unzip

RUN curl -o /tmp/NIFTY_Cloud_api-tools.zip -SL http://cloud.nifty.com/api/sdk/NIFTY_Cloud_api-tools.zip \
	&& unzip /tmp/NIFTY_Cloud_api-tools.zip -d /usr/local/ \
	&& chmod 755 /usr/local/NIFTY_Cloud_api-tools/bin/*

ENV NIFTY_CLOUD_HOME=/usr/local/NIFTY_Cloud_api-tools
ENV PATH=$PATH:$NIFTY_CLOUD_HOME/bin
ENV JAVA_HOME=/usr
ENV JAVA_OPTS=-Duser.language=ja
