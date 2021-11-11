FROM amd64/python:3.9.7-slim-buster

# Version: 9.2.3
ARG MQ_VERSION=923
ARG MQ_TEMP_DIR_PATH=/tmp/mq
ARG MQ_PACKAGES_PATH=$MQ_TEMP_DIR_PATH/MQServer

RUN apt-get update \
    && apt-get install wget -y \
    && apt-get clean

WORKDIR $MQ_TEMP_DIR_PATH
RUN wget https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqadv/mqadv_dev${MQ_VERSION}_ubuntu_x86-64.tar.gz \
    && tar -xf mqadv_dev${MQ_VERSION}_ubuntu_x86-64.tar.gz \
    # needed to change flag to correctly identify system architecture
    && sed -i 's/UNAME_FLAG=-i/UNAME_FLAG=-m/g' $MQ_PACKAGES_PATH/mqlicense.sh

WORKDIR $MQ_PACKAGES_PATH
# license acceptance is required to install packages
RUN ./mqlicense.sh -text_only -accept \
    && dpkg -i ibmmq-runtime_9.2.3.0_amd64.deb \
    && dpkg -i ibmmq-gskit_9.2.3.0_amd64.deb \
    && dpkg -i ibmmq-client_9.2.3.0_amd64.deb \
    && dpkg -i ibmmq-sdk_9.2.3.0_amd64.deb

WORKDIR /
RUN rm -rf $MQ_TEMP_DIR_PATH