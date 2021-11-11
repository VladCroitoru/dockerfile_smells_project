FROM centos/ruby-23-centos7

USER root

RUN \
yum -y install epel-release && \
yum repolist && \
yum install -y firebird-devel && \
yum clean all -y

USER 1001
