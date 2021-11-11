FROM mutterio/mini-elasticsearch

ENV PLUGIN $APP_DIR/bin/plugin
RUN $PLUGIN install lukas-vlcek/bigdesk && \
    $PLUGIN install mobz/elasticsearch-head && \
    $PLUGIN install karmi/elasticsearch-paramedic && \
    $PLUGIN install lmenezes/elasticsearch-kopf

#setup consul-template
ADD consul-template_0.11 /bin/consul-template
RUN chmod +x /bin/consul-template
ADD consul-template.conf /tmp/consul-template.conf
ADD config/es_options.tmpl /tmp/config/es_options.tmpl


ENV LOG_LEVEL info
ENV CONSUL_HOST consul
ENV CONSUL_PORT 8500
ENV SERVICE_9200_NAME search
ENV SERVICE_9300_NAME search-gossip
ENV CLUSTER_NAME docker-elasticsearch
ENV ES_HEAP_SIZE 512m

ADD es-entrypoint.sh /es-entrypoint.sh
RUN chmod +x /es-entrypoint.sh

EXPOSE 9200
EXPOSE 9300
CMD ["/es-entrypoint.sh"]
