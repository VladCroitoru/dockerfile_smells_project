FROM phusion/baseimage:0.9.18
MAINTAINER Andrew Yasinsky <andrew@yasinsky.com>

RUN apt-get -y update\
 && apt-get -y upgrade

RUN DEBIAN_FRONTEND=noninteractive  apt-get install -y ganglia-monitor rrdtool gmetad ganglia-webfrontend nginx php5 php5-fpm php5-gd
#RUN /etc/init.d/apache2 stop

RUN DEBIAN_FRONTEND=noninteractive apt-get remove --purge apache2 && sudo apt-get autoclean && sudo apt-get autoremove
RUN chown -R www-data:www-data /usr/share/ganglia-webfrontend/
RUN rm -rf /var/www/html/
RUN rm /etc/nginx/sites-available/default
RUN rm /etc/nginx/sites-enabled/default
ADD conf/etc/nginx/sites-enabled/ganglia /etc/nginx/sites-enabled/ganglia
ADD conf/etc/nginx/nginx.conf /etc/nginx/nginx.conf

#first stop main gmond (ganglia-monitor) and gmetad processes
RUN stop ganglia-monitor
RUN stop gmetad
#we will be replacing startups with runit
RUN rm /etc/init/gmetad.conf
RUN rm /etc/init/ganglia-monitor.conf
RUN rm /etc/init/php5-fpm.conf

#replace startups with runit
ADD conf/etc/ganglia/gmetad.conf /etc/ganglia/gmetad.conf
ADD conf/etc/ganglia/gmond.conf /etc/ganglia/gmond.conf

#runit daemons
ADD conf/etc/service/ganglia-monitor/run /etc/service/ganglia-monitor/run
ADD conf/etc/service/gmetad/run /etc/service/gmetad/run
ADD conf/etc/service/php5-fpm/run /etc/service/php5-fpm/run
ADD conf/etc/service/nginx/run /etc/service/nginx/run
#start script
ADD conf/etc/my_init.d/01_conf_init.sh /etc/my_init.d/01_conf_init.sh

# cleanup
RUN apt-get clean\
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#UTC timezone
RUN echo "Etc/UTC" | tee /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# defaults
EXPOSE 80 8649 

VOLUME ["/var/lib/ganglia", "/etc/ganglia", "/etc/nginx", "/etc/logrotate.d", "/var/log"]
WORKDIR /
ENV HOME /root
CMD ["/sbin/my_init"]
