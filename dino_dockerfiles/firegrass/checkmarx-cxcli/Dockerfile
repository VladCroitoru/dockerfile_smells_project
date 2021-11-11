FROM openjdk:latest

MAINTAINER Patrick McEvoy <patrick.mcevoy@gmail.com>

ARG CHECKMARX_CX_CLI_URL="http://download.checkmarx.com/8.2.0/Plugins/CxConsolePlugin-CLI-7.5.0.3.zip"

RUN wget -q ${CHECKMARX_CX_CLI_URL} -O /tmp/cli.zip && \
  unzip /tmp/cli.zip -d /opt/ && \
  ln -s /opt/CxConsolePlugin* /opt/CxConsolePlugin && \
  chmod +x /opt/CxConsolePlugin/runCxConsole.sh

VOLUME /usr/src
WORKDIR /usr/src

CMD ["/opt/CxConsolePlugin/runCxConsole.sh", "--help"]
