#
#   Author: Rohith (gambol99@gmail.com)
#   Date: 2015-01-09 16:07:41 +0000 (Fri, 09 Jan 2015)
#
#  vim:ts=2:sw=2:et
#
FROM centos
MAINTAINER Rohith <gambol99@gmail.com>

ADD vulcan_registrator /opt/vulcan_registrator/vulcan_registrator
ADD lib /opt/vulcan_registrator/lib
ADD stage/startup.sh /startup.sh

RUN chmod +x /startup.sh;
RUN yum install -y ruby
RUN gem install -V docker docker-api etcd optionscrapper

ENTRYPOINT [ "/startup.sh" ]
