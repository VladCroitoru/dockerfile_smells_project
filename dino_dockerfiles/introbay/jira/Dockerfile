# Install Atlassian Jira
# This is a trusted build based on the "base" image
FROM ubuntu:18.04

MAINTAINER Ignacio López Flores ignacio@introbay.com

ENV AppName jira-software
ENV AppVer 8.3.3
ENV Arch x64

# Fetch the files
ADD https://www.atlassian.com/software/jira/downloads/binary/atlassian-$AppName-$AppVer-$Arch.bin /opt
ADD ./install_cmds.sh /install_cmds.sh
ADD ./response.varfile /opt/response.varfile
ADD ./init.sh /init.sh

# Install dependencies
RUN apt-get update && apt-get install -y fontconfig \
	&& rm -rf /var/lib/apt/lists/*

## Now Install Atlassian Jira
RUN /install_cmds.sh

# Start the service
CMD ["sh", "/init.sh"]
EXPOSE 8080
VOLUME ["/opt/atlassian/jira-home"]
