FROM frosner/java

MAINTAINER Frank Rosner <frank@fam-rosner.de>

RUN curl -s https://download.elastic.co/logstash/logstash/logstash-2.3.1.tar.gz | tar -xz -C /usr/local \
  && mv /usr/local/logstash-2.3.1 /usr/local/logstash

ADD ddq-logstash.conf /usr/local/logstash/ddq-logstash.conf

RUN mkdir /etc/service/logstash
ADD start-logstash.sh /etc/service/logstash/run
RUN chmod a+x /etc/service/logstash/run

CMD ["/sbin/my_init"]
