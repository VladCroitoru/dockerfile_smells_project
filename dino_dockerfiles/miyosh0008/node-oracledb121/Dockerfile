# Dockerfile
FROM centos:centos7

ENV OCI_LIB_DIR /opt/oracle/instantclient/instantclient_12_1
ENV OCI_INC_DIR /opt/oracle/instantclient/instantclient_12_1/sdk/include

COPY instantclient-basic-linux.x64-*.zip instantclient-sdk-linux.x64-*.zip /tmp/

RUN yum -y update && \
    yum -y install libaio unzip zip gcc gcc-c++ make git python-devel && \
    useradd node -p '$6$salt$ZjJzVKp5xtoIl7cfXqZe0mQjWeOpsV2pMiIYpWzkR4ExCBpPdT3mi3eXtG1MSawJnZfXFjBcq0UUmenLq1Cj//' && \
    curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - && \
    yum -y install nodejs && \
    cd /etc/yum.repos.d && curl -O https://dl.yarnpkg.com/rpm/yarn.repo && \
    yum -y install yarn && \
    mkdir -p /opt/oracle/instantclient && \
    unzip /tmp/instantclient-basic-linux.x64-*.zip -d /opt/oracle/instantclient/ && \
    unzip /tmp/instantclient-sdk-linux.x64-*.zip -d /opt/oracle/instantclient/ && \
    cd /opt/oracle/instantclient/instantclient_12_1 && \
    ln -s libclntsh.so.12.1 libclntsh.so && \
    ln -s libocci.so.12.1 libocci.so && \
    echo "/opt/oracle/instantclient/instantclient_12_1" >/etc/ld.so.conf.d/oracle.conf && \
    echo "export ORACLE_HOME=/opt/oracle/instantclient/instantclient_12_1" >>~/.bash_profile && \
    echo "export LD_LIBRARY_PATH=\$ORACLE_HOME" >>~/.bash_profile && source ~/.bash_profile && \
    npm install -g oracledb --unsafe && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    unlink /etc/localtime && \
    ln -s /usr/share/zoneinfo/Japan /etc/localtime && \
    cd ~ && yum clean all && rm -rf /var/cache/yum && rm -rf /tmp/*

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV HOME /root

CMD ["/bin/bash"]
