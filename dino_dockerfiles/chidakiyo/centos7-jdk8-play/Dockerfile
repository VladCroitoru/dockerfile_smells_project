#
# VERSION 0.0.1
#

FROM chidakiyo/centos7-oracle-jdk8
MAINTAINER chidakiyo "chidakiyo@gmail.com"

# add package
RUN yum -y install unzip

# activator
RUN wget http://downloads.typesafe.com/typesafe-activator/1.3.5/typesafe-activator-1.3.5.zip -P /var/tmp
RUN unzip /var/tmp/typesafe-activator-1.3.5.zip -d /usr/local
RUN ln -s /var/tmp/activator-1.3.5/activator /usr/local/activator

# Set Environment
ENV        PATH         /bin:/usr/bin:/usr/local/scala/bin:/usr/local/activator/bin/

