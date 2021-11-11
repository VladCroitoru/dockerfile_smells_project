FROM ubuntu:15.04
MAINTAINER kumaranjv061990<kumaranjv061990@gmail.com>

#Oracle Java 8
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python-software-properties software-properties-common wget vim curl
RUN add-apt-repository -y ppa:webupd8team/java
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get update && apt-get install -y oracle-java8-installer
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

#ElasticSearch
RUN wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.5.1.deb
RUN dpkg -i elasticsearch-1.5.1.deb
RUN /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head
RUN /usr/share/elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf
RUN /usr/share/elasticsearch/bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.5.0
RUN apt-get update
EXPOSE 9200 9300 9091 

#Kibana
RUN \
    curl -s https://download.elastic.co/kibana/kibana/kibana-4.0.2-linux-x64.tar.gz | tar -C /opt -xz && \
    mv /opt/kibana-4.0.2-linux-x64 /opt/kibana
EXPOSE 5601

#Add start command

ADD start /start 
RUN chmod +x /start
CMD /start
