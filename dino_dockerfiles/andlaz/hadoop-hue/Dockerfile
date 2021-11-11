FROM centos:7.1.1503
MAINTAINER andras.szerdahelyi@gmail.com

RUN useradd hadoop
ADD https://dl.dropboxusercontent.com/u/730827/hue/releases/3.8.1/hue-3.8.1.tgz /home/hadoop/

RUN yum install -y ruby-2.0.0.598 \
		rubygems-2.0.14 \
		python-2.7.5-18.el7_1.1 \
		python-setuptools-0.9.8 \
		tar \
		gzip
		
RUN gem install thor

RUN yum install -y rsync \
	gcc-c++ \
	make \
	python-devel \
	krb5-devel \
	krb5-libs \
	libxml2-devel \
	libxslt-devel \
	sqlite-devel \
	openssl-devel \
	openldap-devel \
	mysql-devel \
	gmp-devel \
	cyrus-sasl-devel \
	&& cd /home/hadoop && tar xf hue-3.8.1.tgz && cd hue-3.8.1 \
	&& make install \
	&& rm -fR /home/hadoop/hue-3.8.1
	
ADD etc/hue/* /etc/hue/
RUN rm -fR /usr/local/hue/desktop/conf && ln -s /etc/hue /usr/local/hue/desktop/conf
ADD entrypoint.sh /root/entrypoint.sh
ADD configure.rb /root/configure.rb



RUN chown -R hadoop /usr/local/hue

EXPOSE 8888

ENTRYPOINT ["/root/entrypoint.sh"]
