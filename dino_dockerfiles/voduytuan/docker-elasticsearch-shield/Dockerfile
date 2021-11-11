FROM elasticsearch:2.3

MAINTAINER Vo Duy Tuan <tuanmaster2012@gmail.com>

# The shield plugin configuration must be in ES_HOME/config
RUN cat config/elasticsearch.yml > /etc/elasticsearch/elasticsearch.yml
RUN rm -rf config
RUN ln -s /etc/elasticsearch/ config

# Install plugins
RUN plugin install license
RUN plugin install shield


ENV ES_USERNAME es_admin
ENV ES_PASSWORD es_adminpassword

COPY es-entrypoint.sh /
ENTRYPOINT ["/es-entrypoint.sh"]
CMD ["elasticsearch"]
