FROM ubuntu:latest
MAINTAINER Peter Grace, pete.grace@gmail.com
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN /usr/bin/add-apt-repository ppa:webupd8team/java
RUN apt-get update
RUN /bin/echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y supervisor unzip git oracle-java7-installer oracle-java7-set-default apache2
RUN apt-get -y upgrade
ADD docker/supervisor-system.conf /etc/supervisor/conf.d/system.conf

#Serf
ADD docker/supervisor-serf.conf /etc/supervisor/conf.d/serf.conf
ADD https://dl.bintray.com/mitchellh/serf/0.6.1_linux_amd64.zip /opt/downloads/
WORKDIR /opt/downloads
RUN ["/bin/bash","-c","unzip 0.6.1_linux_amd64.zip"]
RUN mv /opt/downloads/serf /usr/bin
ADD docker/serf-start.sh /opt/sei-bin/
ADD docker/serf-join.sh /opt/sei-bin/


VOLUME ["/var/lib/elasticsearch/"]
#Elasticsearch
ADD https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.2.deb /opt/downloads/
ADD docker/supervisor-elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf

#logstash
ADD https://download.elasticsearch.org/logstash/logstash/packages/debian/logstash_1.4.2-1-2c0f5a1_all.deb /opt/downloads/
#install both debs and resolve dependencies
RUN /usr/bin/dpkg -i /opt/downloads/elasticsearch-1.3.2.deb /opt/downloads/logstash_1.4.2-1-2c0f5a1_all.deb

#Put logstash files in proper places
ADD http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz /etc/logstash/
RUN /bin/gzip -d /etc/logstash/GeoLiteCity.dat
ADD docker/supervisor-logstash.conf /etc/supervisor/conf.d/logstash.conf
ADD docker/input-supervisor.conf /etc/logstash/conf.d/input-supervisor.conf
ADD docker/input-syslog.conf /etc/logstash/conf.d/input-syslog.conf
ADD docker/output-elastic.conf /etc/logstash/conf.d/output-elastic.conf
ADD docker/filter-haproxy.conf /etc/logstash/conf.d/filter-haproxy.conf
ADD docker/filter-failedpass.conf /etc/logstash/conf.d/filter-failedpass.conf
ADD docker/start-logstash.sh /opt/logstash/
ADD docker/patterns/ /etc/logstash/patterns

#kibana
ADD docker/supervisor-httpd.conf /etc/supervisor/conf.d/httpd.conf
RUN /usr/sbin/a2dissite 000-default
ADD docker/kibana-vhost.conf /etc/apache2/sites-available/0-kibana.conf
RUN /usr/sbin/a2ensite 0-kibana
RUN /usr/sbin/groupadd kibana
RUN /usr/sbin/useradd -d /home/kibana -g kibana -G www-data -m -s /usr/sbin/nologin kibana
ADD https://download.elasticsearch.org/kibana/kibana/kibana-3.1.0.tar.gz /opt/downloads/
RUN mkdir /home/kibana/html
WORKDIR /home/kibana/html
RUN /bin/tar xzvf /opt/downloads/kibana-3.1.0.tar.gz
RUN mv /home/kibana/html/kibana-3.1.0/* /home/kibana/html
RUN rmdir /home/kibana/html/kibana-3.1.0
RUN chown -R kibana:www-data /home/kibana/html

#Fix perms on /var/log/supervisor so logstash can read/write to dir
RUN mkdir -p /var/log/supervisor
RUN chown logstash:logstash /var/log/supervisor
RUN chmod 2770 /var/log/supervisor

#Fire up crontab
RUN /bin/echo -ne "* * * * *\troot\t/bin/kill -USR2 1\n" >> /etc/crontab
ADD docker/supervisor-cron.conf /etc/supervisor/conf.d/cron.conf

CMD ["/usr/bin/supervisord"]
#CMD ["/bin/bash"]
EXPOSE 80/tcp 2000/tcp 9200/tcp 514/tcp 514/udp
