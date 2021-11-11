FROM debian:wheezy
MAINTAINER Tiago Lopes da Costa <tiagolo@gmail.com>

ENV MYSQL_HOME /var/lib/mysql
ENV JENKINS_HOME /var/jenkins_home
ENV NEXUS_HOME /sonatype-work

RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins

VOLUME $MYSQL_HOME
VOLUME $NEXUS_HOME
VOLUME $JENKINS_HOME

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]
