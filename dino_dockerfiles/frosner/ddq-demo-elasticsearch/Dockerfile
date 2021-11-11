FROM frosner/java

MAINTAINER Frank Rosner <frank@fam-rosner.de>

RUN useradd -ms /bin/bash elasticsearch

RUN curl -s https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.1/elasticsearch-2.3.1.tar.gz | tar -xz -C /usr/local \
  && mv /usr/local/elasticsearch-2.3.1 /usr/local/elasticsearch
ADD elasticsearch.yml /usr/local/elasticsearch/config/elasticsearch.yml
RUN chown -R elasticsearch /usr/local/elasticsearch

RUN mkdir /etc/service/elasticsearch
ADD start-elasticsearch.sh /etc/service/elasticsearch/run
RUN chmod a+x /etc/service/elasticsearch/run
RUN chown -R elasticsearch /etc/service/elasticsearch

CMD ["/sbin/my_init"]
