FROM napolitano/docker-centos7-jre8

MAINTAINER Axel Napolitano <docker.2015@skjt.de>

VOLUME ["/var/lib/teamcity"]

ENV TEAMCITY_VERSION 9.1.4
ENV TEAMCITY_SERVER_MEM_OPTS -Xmx750m -XX:MaxPermSize270m
ENV TEAMCITY_DATA_PATH /var/lib/teamcity

RUN yum -y install wget && \
	wget http://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.tar.gz && \
	echo "86766b3b813cdfdd22cd26248d57c8fc71b3178a4dc74e113bc53bd73e8ad5cf	*TeamCity-$TEAMCITY_VERSION.tar.gz" >> SHA256SUM && \
	sha256sum -c SHA256SUM && \
	rm -f SHA256SUM && \
	tar -xvzf TeamCity-$TEAMCITY_VERSION.tar.gz && \
	rm -f TeamCity-$TEAMCITY_VERSION.tar.gz && \
	yum -y remove wget

EXPOSE 8111

CMD TeamCity/bin/teamcity-server.sh run