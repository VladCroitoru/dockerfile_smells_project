# Linux OS
FROM centos:centos7

# Maintainer
MAINTAINER zorino <maximilien1er@gmail.com>

# Install virtuoso + dependencies
RUN yum update -y && \
    yum install -y autoconf automake libtool flex bison \
      gperf gawk m4 make openssl openssl-devel net-tools \
 && mkdir /mnt/graphs \
 && cd /opt/ \
 && curl -L https://github.com/openlink/virtuoso-opensource/releases/download/v7.2.4.2/virtuoso-opensource-7.2.4.2.tar.gz \
    | tar xvz \
 && mv virtuoso-opensource-7.2.4.2 virtuoso-opensource \
 && cd /opt/virtuoso-opensource && bash autogen.sh \
 && ./configure --prefix=/opt/virtuoso-build --enable-fct-vad \
 && make && make install && chmod -R 755 /opt/virtuoso-build/bin/ \
 && rm -fr /opt/virtuoso-opensource/ \
 && yum -y remove git \
 && yum clean all

COPY vt-utils /opt/virtuoso-build/bin/
COPY virtuoso* /opt/virtuoso-build/bin/
COPY vt-cmds /opt/virtuoso-build/bin/vt-cmds

# Create volume for graph data
VOLUME /mnt/graphs
WORKDIR /mnt/graphs
ENV PATH /opt/virtuoso-build/bin:$PATH
ENV GRAPH_HOME /mnt/graphs
ENV DBA_PWD dba

# Exec on start
ENTRYPOINT ["virtuoso-entry.sh"]

# Expose Default Port
EXPOSE 9000
