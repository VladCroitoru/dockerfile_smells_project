#
# million12/rabbitmq
#

FROM centos:centos7
MAINTAINER Marcin Ryzycki marcin@m12.io, Przemyslaw Ozgo linux@ozgo.info

RUN \
  yum update -y && \
  yum install -y epel-release && \
  yum install -y rabbitmq-server && \
  rabbitmq-plugins enable rabbitmq_management && \
  yum clean all

ADD container-files /

EXPOSE 5672 15672

ENTRYPOINT ["/bootstrap.sh"]
