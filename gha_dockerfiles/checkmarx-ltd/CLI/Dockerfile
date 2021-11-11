FROM openjdk:8-jdk-alpine

WORKDIR /opt/cxcli

ARG CLI_VERSION
ENV CLI_VERSION_ENV=$CLI_VERSION

COPY /target/CxConsolePlugin-${CLI_VERSION_ENV}.zip ./cxcli.zip

RUN unzip cxcli.zip && \
    rm -rf cxcli.zip && \
    chmod +x runCxConsole.sh

CMD ["sh", "./runCxConsole.sh"]
