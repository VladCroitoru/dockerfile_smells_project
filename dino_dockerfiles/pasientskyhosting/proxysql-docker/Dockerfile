FROM centos:7
MAINTAINER Joakim Karlsson <jk@patientsky.com>

RUN yum -y update && yum clean all

RUN curl -s https://packagecloud.io/install/repositories/imeyer/runit/script.rpm.sh | bash
RUN rpmkeys --import https://www.percona.com/downloads/RPM-GPG-KEY-percona
RUN yum install -y https://github.com/sysown/proxysql/releases/download/v1.3.3/proxysql-1.3.3-1-centos7.x86_64.rpm
RUN yum install -y http://www.percona.com/downloads/percona-release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm
RUN yum install -y Percona-Server-client-56 runit && yum clean all

COPY bin/jq /usr/bin/jq
RUN chmod a+x /usr/bin/jq

COPY scripts/clusterwatch.sh /clusterwatch.sh
RUN chmod a+x /clusterwatch.sh

COPY services/proxysql /etc/service/proxysql/run
RUN chmod a+x /etc/service/proxysql/run

COPY services/clusterwatch /etc/service/clusterwatch/run
RUN chmod a+x /etc/service/clusterwatch/run

COPY template/proxysql.tmpl /etc/proxysql.tmpl

VOLUME /var/lib/proxysql

EXPOSE 3306 6032
ONBUILD RUN yum update -y

ENTRYPOINT ["/usr/sbin/runsvdir"]
CMD ["-P", "/etc/service"]

