FROM centos:7

ENV GREMLIN_HOME /opt/gremlin

RUN yum -y update \
    && yum -y install epel-release \
    && yum -y install \
        nmap-ncat \
        python-pip \
        python-devel \
        java-1.8.0-openjdk \
        which \
        sudo \
    && yum -y groupinstall "Development Tools" \
    && pip install --upgrade pip

RUN cd /tmp \
    && curl -L -O https://www.apache.org/dist/tinkerpop/3.2.5/apache-tinkerpop-gremlin-server-3.2.5-bin.zip \
    && unzip apache-tinkerpop-gremlin-server-3.2.5-bin.zip \
    && mv apache-tinkerpop-gremlin-server-3.2.5 ${GREMLIN_HOME} \
    && rm *.zip \
    && cd ${GREMLIN_HOME} \
    && bin/gremlin-server.sh -i org.apache.tinkerpop gremlin-python 3.2.5

EXPOSE 8182

WORKDIR ${GREMLIN_HOME}
CMD ["bin/gremlin-server.sh","conf/gremlin-server-modern-py.yaml"]