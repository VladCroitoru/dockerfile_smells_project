FROM node:9.10.0

ENV NPM_CONFIG_LOGLEVEL error

# Install Oracle client
RUN mkdir -p opt/oracle
WORKDIR /opt/oracle
COPY ./oracle/ ./

RUN npm install -g node-gyp && \
    apt-get update && \
    apt-get install libaio1 build-essential unzip curl -y && \
    unzip instantclient-basic-linux.x64-12.2.0.1.0.zip && \
    unzip instantclient-sdk-linux.x64-12.2.0.1.0.zip && \
    rm instantclient-basic-linux.x64-12.2.0.1.0.zip instantclient-sdk-linux.x64-12.2.0.1.0.zip && \
    mv instantclient_12_2 instantclient && \
    cd instantclient && \
    ln -s libclntsh.so.12.1 libclntsh.so

ENV LD_LIBRARY_PATH="/opt/oracle/instantclient"
ENV OCI_HOME="/opt/oracle/instantclient"
ENV OCI_LIB_DIR="/opt/oracle/instantclient"
ENV OCI_INCLUDE_DIR="/opt/oracle/instantclient/sdk/include"

RUN echo '/opt/oracle/instantclient/' | tee -a /etc/ld.so.conf.d/oracle_instant_client.conf && ldconfig
