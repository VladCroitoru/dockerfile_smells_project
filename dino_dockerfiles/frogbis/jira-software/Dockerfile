FROM debian:stretch-slim

ARG JIRA_VERSION=7.13.1

WORKDIR /root/

RUN apt-get update \
	&& apt-get install -y wget \
	&& wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-"${JIRA_VERSION}"-x64.bin \
	&& chmod 700 atlassian-jira-software-"${JIRA_VERSION}"-x64.bin

ADD response.varfile /opt/atlassian/jira/.install4j/response.varfile

RUN bash +x /root/atlassian-jira-software-"${JIRA_VERSION}"-x64.bin -q -varfile /opt/atlassian/jira/.install4j/response.varfile \
	&& rm -f atlassian-jira-software-"${JIRA_VERSION}"-x64.bin

RUN sed -i 's/JVM_MINIMUM_MEMORY="384m"/JVM_MINIMUM_MEMORY="1024m"/g' /opt/atlassian/jira/bin/setenv.sh \
	&& sed -i 's/JVM_MAXIMUM_MEMORY="768m"/JVM_MAXIMUM_MEMORY="2048m"/g' /opt/atlassian/jira/bin/setenv.sh

ENTRYPOINT /opt/atlassian/jira/bin/start-jira.sh -fg
