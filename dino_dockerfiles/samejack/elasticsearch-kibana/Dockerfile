FROM ubuntu:14.04.4
MAINTAINER SJ <sj@toright.com>

# Surpress Upstart errors/warning
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Install package
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get upgrade -y
RUN apt-get -y install software-properties-common
RUN apt-get -y install supervisor

# Install ElasticSearch (Java 8)
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' > /etc/apt/sources.list.d/webupd8team-java.list && \
    echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --recv-keys --keyserver keyserver.ubuntu.com EEA14886 && \
    apt-get update && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections && \
    apt-get -y install oracle-java8-installer

# Install ElasticSearch (ElasticSearch 5.4.3)
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.4.3.deb && \
    dpkg -i elasticsearch-5.4.3.deb && \
    rm elasticsearch-5.4.3.deb

# Install ElasticSearch (IK Plugin 5.4.3)
RUN wget https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v5.4.3/elasticsearch-analysis-ik-5.4.3.zip && \
    mkdir /usr/share/elasticsearch/plugins/ik  && \
    mv elasticsearch-analysis-ik-5.4.3.zip /usr/share/elasticsearch/plugins/ik && \
    cd /usr/share/elasticsearch/plugins/ik/ && \
    apt install -y unzip && \
    unzip elasticsearch-analysis-ik-5.4.3.zip && \
    rm elasticsearch-analysis-ik-5.4.3.zip

# Install ElasticSearch (Kibana 5.4.3)
RUN wget https://artifacts.elastic.co/downloads/kibana/kibana-5.4.3-amd64.deb && \
    dpkg -i kibana-5.4.3-amd64.deb && \
    rm kibana-5.4.3-amd64.deb

# Clear
RUN apt-get remove --purge -y software-properties-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean && \
    echo -n > /var/lib/apt/extended_states && \
    rm -rf /usr/share/man/?? && \
    rm -rf /usr/share/man/??_*

# public host
RUN sed -i.`date +%F` "s/#network.host: 192.168.0.1/network.host: 0.0.0.0/g" /etc/elasticsearch/elasticsearch.yml
RUN sed -i -e 's/#server.host: "localhost"/server.host: "0.0.0.0"/' /etc/kibana/kibana.yml

# install super dictionary(chinese)
ADD conf/main.dic /usr/share/elasticsearch/plugins/ik/config/main.dic

# Init supervisor
ADD conf/supervisord.conf      /etc/supervisor/supervisord.conf
ADD conf/sv-kibana.conf        /etc/supervisor/conf.d
ADD conf/start.sh              /

# Expose Ports
EXPOSE 5601
EXPOSE 9200

CMD ["/start.sh"]
