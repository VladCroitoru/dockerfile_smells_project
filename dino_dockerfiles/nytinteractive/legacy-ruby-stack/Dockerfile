FROM buildpack-deps:wheezy

COPY ./ruby-enterprise-1.8.7-2012.02.tar.gz /usr/local/src/ruby-enterprise-1.8.7-2012.02.tar.gz
RUN cd /usr/local/src && \
	tar -xzf ruby-enterprise-1.8.7-2012.02.tar.gz && \
	cd ruby-enterprise-1.8.7-2012.02 && \
	CFLAGS="-O2 -fno-tree-dce -fno-optimize-sibling-calls" ./installer -a /usr/local --no-dev-docs --dont-install-useful-gems && \
	cd /usr/local/src && \
	rm -rf ruby-enterprise-1.8.7-2012.02

RUN gem install bundler --no-ri --no-rdoc
ADD ./gem /gem
RUN cd /gem && \
	bundle install --local --system

RUN apt-get update && apt-get install -y apache2-mpm-prefork apache2-prefork-dev libapr1-dev libaprutil1-dev
RUN passenger-install-apache2-module -a
COPY ./passenger.conf /etc/apache2/conf.d/passenger

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
CMD ["apache2", "-D", "FOREGROUND"]
EXPOSE 80
