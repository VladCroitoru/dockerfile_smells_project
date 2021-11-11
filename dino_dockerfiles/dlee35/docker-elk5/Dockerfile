############################################################
# Dockerfile to build Elastic Stack 5 containers
# Based on Ubuntu 16.04
# Listens on 5514/TCP for Beats input for Bro lgos
############################################################

# Set the base image to Ubuntu
FROM ubuntu:16.04

# File Author / Maintainer
MAINTAINER Dustin Lee dlee35@gmail.com

################## BEGIN INSTALLATION ######################

# Update and install required dependencies
RUN DEBIAN_FRONTEND=noninteractive && \
 apt-get -qq update && \
 apt-get install -qq wget supervisor git nginx \
 curl software-properties-common logrotate

# Satisfy Java 8 requirement
RUN DEBIAN_FRONTEND=noninteractive && \
 add-apt-repository ppa:webupd8team/java && \
 apt-get -qq update && \
 echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
 apt-get install -y oracle-java8-installer

# Download and install Alpha 1 binaries (will update based on Elastic release)
RUN wget https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/5.0.0-alpha1/elasticsearch-5.0.0-alpha1.deb && \
 wget https://download.elastic.co/kibana/kibana/kibana_5.0.0-alpha1_amd64.deb && \
 wget https://download.elastic.co/logstash/logstash/packages/debian/logstash_5.0.0~alpha1-1_all.deb && \
 wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && \
 git clone https://github.com/dlee35/docker-elk5.git

# Install packages and remove binaries
RUN dpkg -i elasticsearch-5.0.0-alpha1.deb && \
 dpkg -i kibana_5.0.0-alpha1_amd64.deb && \
 dpkg -i logstash_5.0.0~alpha1-1_all.deb && \
 gunzip GeoLiteCity.dat.gz && \
 rm *.deb

# Install desired plugins for massaging of the data
RUN /opt/logstash/bin/logstash-plugin install logstash-input-beats && \
 /opt/logstash/bin/logstash-plugin install logstash-filter-translate && \
 /opt/logstash/bin/logstash-plugin install logstash-filter-geoip

# Move GeoLiteCity to default dir
RUN mkdir -p /usr/share/GeoIP && \
 mv GeoLiteCity.dat /usr/share/GeoIP/.

# Simple configuration files for standard operation
RUN mv /docker-elk5/10_input.conf /docker-elk5/20_filter.conf \
 /docker-elk5/90_output.conf /etc/logstash/conf.d/

# Script that creates static mapping in Elastic prior to log ingestion
RUN mv /docker-elk5/createmapping.sh /docker-elk5/createcert.sh /etc/init.d/ && \
 mv /docker-elk5/default /etc/nginx/sites-available/default && \
 mv /docker-elk5/htpasswd.users /etc/nginx/htpasswd.users

# Create directory for bro patterns, adjust configs to fix logstash falling over before start
# (see this link for more: https://github.com/elastic/logstash/pull/5083),
# base Elastic's yaml to run locally and require just one master node 
# start Elastic to run static mapping script
RUN mkdir /etc/logstash/patterns && \
 chmod +x /etc/init.d/createmapping.sh && \
 chmod +x /etc/init.d/createcert.sh && \
 sed -i 's/agent\ //' /etc/init.d/logstash && \
 sed -i -e '/^#\ network.host.* /s/^#\ //' -e '/^network.host.* /s/192.168.0.1/localhost/' \
 -e '/^#\ discovery.zen.minimum.* /s/^#\ //' -e '/master_nodes:\ 3$/ s/3/1/' \
 /etc/elasticsearch/elasticsearch.yml && \
 sed -i -e '/^#\ server.ssl.cert.*/c\ server.ssl.cert\:\ \/etc\/ssl\/certs\/elk.local.pem' \
 -e '/^#\ server.ssl.key.* /c\ server.ssl.key\:\ \/etc\/ssl\/private\/elk.local.key' \
 /opt/kibana/config/kibana.yml

# Pushed this into a separate action for testing
# Have to find a better way to allow kibana access to key....
RUN /bin/bash /etc/init.d/elasticsearch start && \
 sleep 20 && \
 /bin/bash /etc/init.d/createmapping.sh && \
 /bin/bash /etc/init.d/createcert.sh && \
 chown -R kibana /etc/ssl/private/

# Bro patterns slightly altered and allow supervisor to manage the processes
RUN mv /docker-elk5/bro /etc/logstash/patterns/bro && \
 mv /docker-elk5/supervisor.conf /etc/supervisor/conf.d/supervisor.conf && \
 rm -rf /docker-elk5

EXPOSE 443 5514 5601 

CMD ["/usr/bin/supervisord"]
