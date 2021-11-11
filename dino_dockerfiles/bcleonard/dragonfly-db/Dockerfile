FROM centos:7.1.1503
MAINTAINER Bradley Leonard <bradley@stygianresearch.com>

# install hostname, mariadb-server, mariadb, psmisc & wget
RUN yum -y update\
 && yum -y install --setopt=tsflags=nodocs bind-utils hostname mariadb-server psmisc wget\
 && yum clean all

#
# download the TESTDB.SQL code
#
ENV URL=https://raw.githubusercontent.com/FlatBallFlyer/IBM-Data-Merge-Utility/master/idmu-war/src/main/resources/TESTDB.sql
RUN cd /tmp &&\
  wget $URL

#
# add the start up script
# 
ADD ./docker-entrypoint.sh /opt/docker-entrypoint.sh

ENTRYPOINT ["/opt/docker-entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld_safe"]
