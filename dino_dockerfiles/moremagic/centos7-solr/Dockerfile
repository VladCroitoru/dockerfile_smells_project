FROM centos:7
MAINTAINER moremagic<itoumagic@gmail.com>

# Install
RUN yum -y update
RUN yum -y install wget tar java-1.7.0-*

# ssh
RUN yum install -y passwd openssh-server initscripts \
	&& echo 'root:root' | chpasswd \
	&& /usr/sbin/sshd-keygen

# Solr install
RUN wget https://archive.apache.org/dist/lucene/solr/5.4.1/solr-5.4.1.tgz \
	&& tar -zxvf solr-*.tgz \
	&& rm -f solr-*.tgz

EXPOSE 22 8080
CMD /solr-5.4.1/bin/solr start -p 8080; \
	/usr/sbin/sshd -D

