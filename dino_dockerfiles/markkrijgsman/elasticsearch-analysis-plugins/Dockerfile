FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.2
LABEL maintainer="Mark Krijgsman <mark.krijgsman@luminis.eu>"

COPY elastic-cjk-basic-plugin-6.4.2.zip /usr/share/elasticsearch/

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-smartcn
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-kuromoji
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install file:///usr/share/elasticsearch/elastic-cjk-basic-plugin-6.4.2.zip
