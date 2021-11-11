FROM ghoranyi/container-storage:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --force-yes default-jre-headless mysql-server redis-server

RUN curl -L -o /tmp/elasticsearch.tar.gz https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.4/elasticsearch-2.3.4.tar.gz
RUN mkdir -p /opt/elasticsearch
RUN tar -xvf /tmp/elasticsearch.tar.gz -C /opt/elasticsearch
RUN useradd -ms /bin/bash elasticsearch
RUN chown -R elasticsearch /opt/elasticsearch

RUN mkdir -p /opt/mysql
ADD init_mysql_server.sh /opt/mysql/

ENV C_FORCE_ROOT=1
ENV CELERY_BROKER_REDIS_URL=localhost
ENV CELERY_RESULTS_REDIS_URL=localhost
ENV ELASTICSEARCH_URL=http://localhost:9200
ENV MYSQL_HOST=localhost

RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install --force-yes -y nodejs

ADD vizceral /opt/vizceral
RUN cd /opt/vizceral && npm install

RUN pip install supervisor

ADD supervisord.conf /etc/supervisor/supervisord.conf
RUN touch /var/run/supervisor.sock
RUN chmod a+rwx /var/run/supervisor.sock

EXPOSE 9200
EXPOSE 8080

CMD /opt/mysql/init_mysql_server.sh && /virtualenv/bin/python /app/manage.py migrate && service redis-server start && supervisord
