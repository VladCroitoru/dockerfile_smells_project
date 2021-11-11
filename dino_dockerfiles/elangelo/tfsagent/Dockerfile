FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install software-properties-common
#adding custom repo for latest git, need at least 2.9.0
RUN apt-add-repository ppa:git-core/ppa

RUN apt-get update

RUN apt-get install -y libunwind8 libcurl3 git gosu

ADD https://github.com/Microsoft/vsts-agent/releases/download/v2.109.2/vsts-agent-ubuntu.16.04-x64-2.109.2.tar.gz /
#COPY vsts-agent-ubuntu.16.04-x64-2.109.2.tar.gz /

COPY imagescripts/docker-entrypoint.sh /docker-entrypoint.sh

RUN mkdir myagent

RUN tar xzf vsts-agent-ubuntu.16.04-x64-2.109.2.tar.gz -C myagent/
RUN chmod 777 /myagent/

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["install"]
