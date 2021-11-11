FROM phusion/baseimage:0.9.22
# Use baseimage-docker's init system
CMD ["/sbin/my_init"]
ENV KILL_PROCESS_TIMEOUT 60
ENV KILL_ALL_PROCESS_TIMEOUT 60

MAINTAINER Kyle Wilcox <kyle@axiomdatascience.com>
ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8

# Setup Riak
ENV OS_FAMILY ubuntu
ENV OS_VERSION 14.04
ENV OS_FLAVOR xenial
ENV RIAK_EXPLORER_VERSION 1.4.1
ENV RIAK_EXPLORER_HOME /riak_explorer
ENV RIAK_EXPLORER_LOGS /var/log/riak_explorer
ENV RIAK_EXPLORER_CONFIG ${RIAK_EXPLORER_HOME}/etc/riak_explorer.conf
ENV RIAK_EXPLORER_USER_CONFIG ${RIAK_EXPLORER_HOME}/etc/user.conf

RUN apt-get update && \
    apt-get install -y \
        binutils \
        build-essential \
        bzip2 \
        ca-certificates \
        curl \
        && \
    mkdir -p ${RIAK_EXPLORER_HOME} && \
    mkdir -p ${RIAK_EXPLORER_LOGS} && \
    curl -sSL https://github.com/basho-labs/riak_explorer/releases/download/${RIAK_EXPLORER_VERSION}/riak_explorer-${RIAK_EXPLORER_VERSION}-${OS_FAMILY}-${OS_VERSION}.tar.gz | tar -zxf - -C ${RIAK_EXPLORER_HOME} --strip-components 1 && \
    groupadd -r riak &&  \
    useradd -r -g riak -d ${RIAK_EXPLORER_HOME} riak && \
    chown -R riak:riak ${RIAK_EXPLORER_HOME} && \
    rm -rf /etc/service/cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH ${RIAK_EXPLORER_HOME}/bin:$PATH

EXPOSE 9000

VOLUME [ "${RIAK_EXPLORER_LOGS}" ]

WORKDIR ${RIAK_EXPLORER_HOME}

COPY init/* /etc/my_init.d/
COPY explorer.sh /etc/service/riak_explorer/run
