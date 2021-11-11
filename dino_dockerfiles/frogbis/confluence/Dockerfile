FROM debian:stretch-slim 

ARG CONFLUENCE_VERSION=5.7.4

WORKDIR /root/

RUN apt-get update &&\
    apt-get install -y wget &&\
    wget https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-"${CONFLUENCE_VERSION}"-x64.bin &&\
    chmod 700 atlassian-confluence-"${CONFLUENCE_VERSION}"-x64.bin

ADD response.varfile /opt/atlassian/confluence/.install4j/response.varfile

RUN bash +x /root/atlassian-confluence-"${CONFLUENCE_VERSION}"-x64.bin -q -varfile /opt/atlassian/confluence/.install4j/response.varfile &&\
    rm -f atlassian-confluence-"${CONFLUENCE_VERSION}"-x64.bin

ENTRYPOINT /opt/atlassian/confluence/bin/start-confluence.sh -fg
