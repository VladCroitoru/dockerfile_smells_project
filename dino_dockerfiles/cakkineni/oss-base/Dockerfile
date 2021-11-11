FROM centos:7

ADD logstash.repo /etc/yum.repos.d/logstash.repo
ADD sensu.repo /etc/yum.repos.d/sensu.repo

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.71-2.b15.el7_2.x86_64/jre

RUN yum -y install epel-release; yum clean all
RUN yum update -y && \
	yum install -y \
	collectd \
	collectd-java \
	collectd-generic-jmx \
	sysstat \
	supervisor \
	logstash \
	ntp \
	rubygems \
	net-tools \
	ruby \
	ruby-devel \
	libgmp-dev \
	gcc \
	make \
	build-essential \
	g++ \
	libxml2 \
	libxml2-devel \
	libxslt \
	libxslt-devel \
	sensu 

RUN yum -y groupinstall "Development Tools"

RUN gem install \
	sensu-plugin \
	carrot-top \
	rest-client \
	bunny \
	redis \
	rspec \
	serverspec \
	--no-ri --no-rdoc

ADD supervisord.base.conf /etc/supervisor/conf.d/supervisor.base.conf
ADD supervisord.conf /etc/supervisor/supervisord.conf

CMD ["supervisord","-n", "-c", "/etc/supervisor/supervisord.conf"]
