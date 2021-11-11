FROM frosner/spark-base

MAINTAINER Frank Rosner <frank@fam-rosner.de>

RUN mkdir /etc/service/streamreader
ADD ddq-demo-spark-assembly-1.0.0.jar /etc/service/streamreader/job.jar
ADD streamreader.sh /etc/service/streamreader/run
RUN chmod a+x /etc/service/streamreader/run

RUN curl -s https://download.elastic.co/beats/filebeat/filebeat-1.2.1-x86_64.tar.gz | tar -xz -C /usr/local \
  && mv /usr/local/filebeat-1.2.1-x86_64 /usr/local/filebeat
ADD filebeat.yml /usr/local/filebeat/filebeat.yml

RUN mkdir /etc/service/filebeat
ADD start-filebeat.sh /etc/service/filebeat/run
RUN chmod a+x /etc/service/filebeat/run

CMD ["/sbin/my_init"]
