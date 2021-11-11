FROM otasys/elk-redis

WORKDIR /opt/logstash
RUN bin/plugin install contrib

RUN apt-get update -qq \
 && apt-get install -qqy python-pip python-dev
RUN pip install docopt \
 && pip install trollius \
 && pip install whisper \
 && pip install carbon

 WORKDIR /opt/graphite/conf
 RUN cp carbon.conf.example carbon.conf
 RUN cp storage-schemas.conf.example storage-schemas.conf

ADD ./logreplay.py /usr/local/bin/
RUN chmod +x /usr/local/bin/logreplay.py
RUN mkdir /tmp/logreplay-input/
ADD ./supervisor/logreplay.conf /etc/supervisor/conf.d/

ADD ./logstash/logstash-indexer.conf /etc/logstash/
ADD ./supervisor/logstash-indexer.conf /etc/supervisor/conf.d/
ADD ./supervisor/carbon.conf /etc/supervisor/conf.d/

CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
