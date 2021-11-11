#
# Databaze dopravnich nehod CR: elasticsearch + kibana
# 
# http://www.ludekvesely.cz/databaze-dopravnich-nehod-cr/
# ludek.vesely@email.com
#
FROM ubuntu
MAINTAINER Ludek Vesely <ludek.vesely@email.com>
ENV KIBANA_VERSION 4.0.2
ENV ES_VERSION 1.5.2
ENV DEBIAN_FRONTEND noninteractive

# Install java 8
RUN apt-get update && apt-get install software-properties-common -y
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update -y
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
RUN apt-get install oracle-java8-installer -y 
RUN update-java-alternatives -s java-8-oracle 
RUN apt-get install oracle-java8-set-default -y

# Install ElasticSearch
RUN wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.deb
RUN dpkg -i elasticsearch-$ES_VERSION.deb
RUN update-rc.d elasticsearch defaults 95 10
RUN echo "cluster.name: nehody" > /etc/elasticsearch/elasticsearch.yml
RUN echo 'node.name: "nehody"' >> /etc/elasticsearch/elasticsearch.yml
RUN echo 'index.number_of_shards: 1' >> /etc/elasticsearch/elasticsearch.yml
RUN echo 'index.number_of_replicas: 0' >> /etc/elasticsearch/elasticsearch.yml
RUN echo 'node.local: true' >> /etc/elasticsearch/elasticsearch.yml
RUN echo 'http.cors.enabled: true' >> /etc/elasticsearch/elasticsearch.yml
RUN rm *.deb

# Install ElasticDump
RUN apt-get update && apt-get install nodejs npm build-essential curl node -y
RUN npm install elasticdump -g 
RUN ls -l /usr/local/lib/node_modules/ 
RUN nodejs /usr/local/lib/node_modules/elasticdump 

# Download and import data
RUN wget http://public.ludekvesely.cz/dopravni-nehody/es-kibana-mapping.json -q; \
	wget http://public.ludekvesely.cz/dopravni-nehody/es-kibana-data.json -q; \
	wget http://public.ludekvesely.cz/dopravni-nehody/es-nehody-mapping.json -q; \
	wget http://public.ludekvesely.cz/dopravni-nehody/es-nehody-data.json -q
RUN /etc/init.d/elasticsearch start; sleep 8; \
	curl --silent -XPUT 'localhost:9200/.kibana'; \
	curl --silent -XPUT 'localhost:9200/nehody'; \
	nodejs /usr/local/lib/node_modules/elasticdump/bin/elasticdump --input es-kibana-mapping.json --output=http://localhost:9200/.kibana --type=mapping; \
	nodejs /usr/local/lib/node_modules/elasticdump/bin/elasticdump --input es-kibana-data.json --output=http://localhost:9200/.kibana --type=data; \
	nodejs /usr/local/lib/node_modules/elasticdump/bin/elasticdump --input es-nehody-mapping.json --output=http://localhost:9200/nehody --type=mapping; \
	nodejs /usr/local/lib/node_modules/elasticdump/bin/elasticdump --input es-nehody-data.json --output=http://localhost:9200/nehody --type=data
RUN rm *.json

# Install Kibana
WORKDIR /root
RUN wget https://download.elastic.co/kibana/kibana/kibana-$KIBANA_VERSION-linux-x64.tar.gz -q
RUN tar xzf kibana-$KIBANA_VERSION-linux-x64.tar.gz
RUN rm kibana-$KIBANA_VERSION-linux-x64.tar.gz
RUN echo '/etc/init.d/elasticsearch start; /root/kibana-'$KIBANA_VERSION'-linux-x64/bin/kibana' >run.sh 

# Run Kibana on port 5601
CMD bash -C '/root/run.sh';'bash'
EXPOSE 5601
