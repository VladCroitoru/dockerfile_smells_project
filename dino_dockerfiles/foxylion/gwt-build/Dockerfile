FROM ubuntu:16.04
MAINTAINER Jakob Jarosch <dev@jakobjarosch.de>

RUN apt-get update && apt-get install -y openjdk-8-jdk git make wget unzip

RUN wget http://ftp.halifax.rwth-aachen.de/apache//ant/binaries/apache-ant-1.9.9-bin.zip
RUN unzip apache-ant-1.9.9-bin.zip
ENV PATH=/apache-ant-1.9.9/bin:$PATH

RUN git clone --depth 1 https://github.com/gwtproject/tools.git /gwt-tools
ENV GWT_TOOLS=/gwt-tools

ENV TZ=America/Los_Angeles
ENV ANT_OPTS=-Dfile.encoding=UTF-8

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
