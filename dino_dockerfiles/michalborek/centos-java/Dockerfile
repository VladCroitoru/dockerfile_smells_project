FROM centos:centos7
MAINTAINER Michal Borek <michal@greenpath.pl>

RUN yum install -y wget && \
yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel && \
yum clean all

RUN useradd --system --shell /usr/sbin/nologin ms 
USER ms 
CMD [ -f /ms/config ] && . /ms/config ; java $MS_JAVA_OPTS -jar "/ms/${MS_JAR_NAME}"
