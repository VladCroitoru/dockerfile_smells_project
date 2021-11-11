FROM debian:jessie

MAINTAINER Dushman Elvitigala <dushmane@brandixi3.com>

RUN DEBIAN_FRONTEND=noninteractive 
RUN apt-get -y clean && apt-get -y autoclean && apt-get -y update && apt-get -y upgrade

WORKDIR /tmp

RUN DEBIAN_FRONTEND=noninteractive 
RUN apt-get install -y vim less nano ntp net-tools inetutils-ping curl telnet supervisor sed

#Install Oracle Java 7
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main' > /etc/apt/sources.list.d/java.list 
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 
RUN apt-get update && echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections 
RUN apt-get install -y oracle-java7-installer

#ElasticSearch
RUN wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.6.0.tar.gz && \
    tar xf elasticsearch-*.tar.gz && \
    rm elasticsearch-*.tar.gz && \
    mv elasticsearch-* /usr/src/elasticsearch

#Kibana
RUN wget https://download.elastic.co/kibana/kibana/kibana-4.1.1-linux-x64.tar.gz && \
    tar xf kibana-*.tar.gz && \
    rm kibana-*.tar.gz && \
    mv kibana-* /usr/src/kibana

#Logstash
RUN wget https://download.elasticsearch.org/logstash/logstash/logstash-1.5.2.tar.gz && \
	tar xf logstash-*.tar.gz && \
    rm logstash-*.tar.gz && \
    mv logstash-* /usr/src/logstash

#Configuration

RUN sed -i -e 's#\#path.conf\: \/path\/to\/conf#path.conf\: \/usr\/src\/elasticsearch\/config#g' /usr/src/elasticsearch/config/elasticsearch.yml
RUN sed -i -e 's#\#path.logs\: \/path\/to\/logs#path.logs\: \/opt\/elk\/logs#g' /usr/src/elasticsearch/config/elasticsearch.yml
RUN sed -i -e 's#\#path.work\: \/path\/to\/work#path.work\: \/opt\/elk\/work#g' /usr/src/elasticsearch/config/elasticsearch.yml

RUN echo path.data\: \/opt\/elk\/data >> /usr/src/elasticsearch/config/elasticsearch.yml

RUN sed -i -e 's#\# log_file\: .\/kibana.log#log_file: \/opt\/elk\/logs\/kibana.log#g' /usr/src/kibana/config/kibana.yml

RUN mkdir /opt/elk
RUN mkdir /opt/elk/conf
RUN mkdir /opt/elk/logs
RUN mkdir /opt/elk/certs
RUN mkdir /opt/elk/data
RUN mkdir /opt/elk/work

ADD supervisord-logstash.conf /etc/supervisor/conf.d/
VOLUME ["/opt/elk/conf", "/opt/elk/logs", "/opt/elk/cert"]

#5601=kibana, 9200=elasticsearch, 49021=logstash, 5043=lumberjack
EXPOSE 5601 9200 49021 5043 
CMD ["/usr/bin/supervisord", "-n"]
