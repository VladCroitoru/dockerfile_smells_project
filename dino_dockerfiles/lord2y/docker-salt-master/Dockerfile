FROM centos:7.1.1503
MAINTAINER Alessandro Ratti <alessandro.ratti@gmail.com>

RUN yum clean all && yum swap -y fakesystemd systemd
RUN yum install -y https://repo.saltstack.com/yum/redhat/salt-repo-latest-1.el7.noarch.rpm && yum install -y salt-master
RUN yum clean all
VOLUME ["/etc/salt/pki", \
        "/etc/salt/master.d", \
        "/etc/salt/cloud.maps.d", \
        "/etc/salt/cloud.conf.d", \
        "/etc/salt/cloud.profiles.d", \
        "/etc/salt/cloud.providers.d", \
        "/etc/salt/minion.d", \
        "/var/cache/salt", \
        "/var/logs/salt", \
        "/srv/salt"]

COPY run.sh /usr/local/bin/
RUN chmod +x \
    /usr/local/bin/run.sh

EXPOSE 4505 4506

CMD /usr/local/bin/run.sh
