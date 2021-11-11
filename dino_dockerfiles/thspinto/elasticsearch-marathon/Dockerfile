FROM elasticsearch:2.4.4

COPY cluster .
COPY start_elasticsearch.sh .
RUN chown elasticsearch  ./config/elasticsearch.yml
USER elasticsearch

EXPOSE 9200 9300
ENTRYPOINT ["./start_elasticsearch.sh"]
