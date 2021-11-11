FROM ubuntu:15.04

MAINTAINER Jostein Austvik Jacobsen

# Set working directory to home directory
WORKDIR /root/

# Set up repositories
RUN apt-get install -y software-properties-common
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list

# Set locale
RUN locale-gen en_GB en_GB.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL C.UTF-8

# Install Java
RUN apt-get update && apt-get install -y openjdk-7-jre openjdk-8-jre
ENV JAVA_7_HOME /usr/lib/jvm/java-7-openjdk-amd64
ENV JAVA_8_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Install some basic tools
RUN apt-get update && apt-get install -y wget unzip curl

# Install some more tools
RUN apt-get update && apt-get install -y maven git subversion mercurial bzr ansible vim make gcc sudo lame

# Pipeline 2 CLI from Pipeline 2 v1.9 (requires Java 7 because the cli refuses to use '1.8.0_45-internal')
RUN wget --no-verbose https://github.com/daisy/pipeline-assembly/releases/download/v1.9/pipeline2-1.9-webui_linux.zip \
    && unzip pipeline2-1.9-webui_linux.zip \
    && mv daisy-pipeline/cli dp2-cli \
    && rm daisy-pipeline pipeline2-*.zip -rf \
    && sed -i 's/starting:.*/starting: false/' dp2-cli/config.yml \
    && mv dp2-cli/dp2 dp2-cli/dp2-cli

COPY src/dp2 /root/dp2-cli/dp2
ENV PATH $PATH:/root/dp2-cli

# Install latest version of the Pipeline 2 engine, braille modules, and Web UI
COPY src/setup.sh /root/setup.sh
COPY roles/test-server/vars/versions.yml /root/versions.yml
RUN /root/setup.sh

# Bind engine to 0.0.0.0 instead of localhost
RUN sed -i 's/org.daisy.pipeline.ws.host=.*/org.daisy.pipeline.ws.host=0.0.0.0/' /opt/daisy-pipeline2/etc/system.properties

EXPOSE 8181 9000

CMD service pipeline2d start && service daisy-pipeline2-webui start && tail -f /var/log/daisy-pipeline2/daisy-pipeline.log
