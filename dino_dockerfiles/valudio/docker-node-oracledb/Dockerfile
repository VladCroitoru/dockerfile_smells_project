FROM python:3.3.6-slim
MAINTAINER Valudio <development@valudio.com>

ADD ./files /opt/oracle

RUN apt-get update \
    && apt-get -y install unzip libaio1 curl make g++ \
    && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get -y install nodejs

RUN cd /opt/oracle && sh start.sh

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/oracle/instantclient

ENV OCI_HOME="/opt/oracle/instantclient"
ENV OCI_LIB_DIR="/opt/oracle/instantclient"
ENV OCI_INCLUDE_DIR="/opt/oracle/instantclient/sdk/include"


EXPOSE 8066
WORKDIR /opt/app

CMD ["bash"]
