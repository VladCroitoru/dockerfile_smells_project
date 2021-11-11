FROM ubuntu:14.04
MAINTAINER skydjol@gmail.com
RUN apt-get install apt-transport-https wget -y && wget http://archive.cloudera.com/cdh5/one-click-install/precise/amd64/cdh5-repository_1.0_all.deb \
&& dpkg -i /cdh5-repository_1.0_all.deb \
&& apt-get update \
&& apt-get install -y  software-properties-common \
&& add-apt-repository ppa:webupd8team/java -y \
&& apt-get update \
&& echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
&& apt-get install -y oracle-java7-installer vim

RUN apt-get install impala impala-server impala-shell impala-catalog impala-state-store -y \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 21000 21050 25000 25010 25020
