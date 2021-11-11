FROM centos:7.3.1611
MAINTAINER Tomas Olivares, tolivares@gmail.com

RUN yum -y update && yum -y install \
  java-1.8.0-openjdk \
  curl \
  && rm -rf /usr/share/doc/* && \
  rm -rf /usr/share/info/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/*

ENV SERPOSCOPE_VERSION 2.7.1

RUN mkdir -p /opt/serposcope /var/log/serposcope /var/lib/serposcope/
RUN curl -L https://serposcope.serphacker.com/download/${SERPOSCOPE_VERSION}/serposcope-${SERPOSCOPE_VERSION}.jar > /opt/serposcope.jar
RUN useradd -u 1000 -d /home/serposcope -m serposcope
COPY serposcope.conf /etc/serposcope.conf
RUN chown -R serposcope:serposcope /var/log/serposcope /var/lib/serposcope/ /etc/serposcope.conf
COPY entrypoint.sh /usr/local/bin/

EXPOSE 7134

USER serposcope

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
