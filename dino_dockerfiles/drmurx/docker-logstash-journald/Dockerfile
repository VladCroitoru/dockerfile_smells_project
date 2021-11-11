FROM docker.elastic.co/logstash/logstash:7.0.0

USER root

RUN curl https://copr.fedorainfracloud.org/coprs/jsynacek/systemd-backports-for-centos-7/repo/epel-7/jsynacek-systemd-backports-for-centos-x7-epel-7.repo > /etc/yum.repos.d/jsynacek-systemd-centos-7.repo \
 && yum -y update systemd

USER logstash

RUN /usr/share/logstash/bin/logstash-plugin install logstash-input-journald
