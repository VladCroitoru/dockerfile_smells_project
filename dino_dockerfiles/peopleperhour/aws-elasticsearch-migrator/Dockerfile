FROM logstash
MAINTAINER Panagiotis Moustafellos <pmoust@peopleperhour.com>

ENV ES_HOSTS    localhost
ENV ES_PORT     9200
ENV ES_SCAN     true
ENV ES_SIZE     1000
ENV ES_SCROLL   5m
ENV ES_INDEX    logstash-*

ENV AWS_ES_HOSTS            search-elk-setMeInYourEnv.us-east-1.es.amazonaws.com
ENV AWS_ACCESS_KEY_ID       KEY
ENV AWS_SECRET_ACCESS_KEY   SECRET
ENV DEFAULT_REGION          us-east-1

COPY logstash.conf.example /
COPY start.sh /

RUN apt-get update && \
    apt-get install -y gettext-base && \
    /opt/logstash/bin/plugin install logstash-output-amazon_es && \
    chmod +x /start.sh

CMD [ "/start.sh" ]
