# Kibana-4 Dockerfile
#
# https://github.com/elasticsearch/kibana
#
 
# Pull base image.
FROM dockerfile/nginx
 
MAINTAINER Ayham Alzoubi "ayham.a.alzoubi@gmail.com"

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
RUN apt-get update
 
# auto accept oracle jdk license
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java7-installer
 
# Install Kibana.
RUN \
  cd /tmp && \
  wget https://download.elasticsearch.org/kibana/kibana/kibana-4.0.0-BETA2.tar.gz && \
  tar xvzf kibana-4.0.0-BETA2.tar.gz && \
  rm -f kibana-4.0.0-BETA2.tar.gz && \
  mv /tmp/kibana-4.0.0-BETA2 /kibana

# Create Config Directory
RUN mkdir -p /settings/ && touch /settings/setup-env.sh
 
COPY . /src
 
RUN rm -rf /etc/nginx/sites-available/default
 
RUN sed -i 's/^daemon off/daemon on/' /etc/nginx/nginx.conf
 
RUN cd /src && chmod +x run.sh
 
EXPOSE 5601
 
CMD . /settings/setup-env.sh && . /src/run.sh && nginx && /kibana/bin/kibana
