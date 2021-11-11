FROM centos:centos6

MAINTAINER Martín González <mgonzalez@codingways.com>

#Add puppetlabs repo
RUN rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm

#Install puppet-server
RUN yum -y install puppet-server

#Install apache2 and rubygems
RUN yum -y install httpd httpd-devel mod_ssl ruby-devel rubygems gcc

#Install Rack/Passenger
RUN gem install rack passenger

#Install Passenger apache2 module dependencies
RUN yum -y install gcc-c++ libcurl-devel openssl-devel zlib-devel

#Install Passenger apache2 module
RUN passenger-install-apache2-module -a --languages ruby

#Load module in apache
RUN echo "LoadModule passenger_module /usr/lib/ruby/gems/1.8/gems/passenger-$(passenger-config --version)/buildout/apache2/mod_passenger.so" | sed 's/Phusion Passenger //' >> /etc/httpd/conf/httpd.conf
RUN echo "<IfModule mod_passenger.c>" >> /etc/httpd/conf/httpd.conf
RUN echo "PassengerRoot /usr/lib/ruby/gems/1.8/gems/passenger-$(passenger-config --version)" | sed 's/Phusion Passenger //' >> /etc/httpd/conf/httpd.conf
RUN echo "PassengerDefaultRuby /usr/bin/ruby" >> /etc/httpd/conf/httpd.conf
RUN echo "</IfModule>" >> /etc/httpd/conf/httpd.conf

#Add setting to puppet.conf
RUN echo -e "\n[master]\nalways_cache_features=true" >> /etc/puppet/puppet.conf

#Install puppet master rack app
RUN mkdir -p /usr/share/puppet/rack/puppetmasterd
RUN mkdir /usr/share/puppet/rack/puppetmasterd/public /usr/share/puppet/rack/puppetmasterd/tmp
RUN cp /usr/share/puppet/ext/rack/config.ru /usr/share/puppet/rack/puppetmasterd/
RUN chown puppet:puppet /usr/share/puppet/rack/puppetmasterd/config.ru

#Copy vhost conf to apache2 dir
ADD puppetmaster.conf /etc/httpd/conf.d/puppetmaster.conf

#Add init script to container
ADD start.sh /start.sh

#Link volumes to host
VOLUME /var/lib/puppet /etc/puppet

#Map port to host
EXPOSE 8140

#Exec init script
CMD /start.sh

