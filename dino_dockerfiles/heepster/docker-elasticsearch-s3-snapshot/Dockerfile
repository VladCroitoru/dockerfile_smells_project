FROM elasticsearch:1.7

RUN /usr/share/elasticsearch/bin/plugin -i mobz/elasticsearch-head
RUN /usr/share/elasticsearch/bin/plugin -i elasticsearch/elasticsearch-cloud-aws/2.7.1

COPY snapshotter.sh /
COPY run.sh /

ENV REPLICA true

EXPOSE 9200 9300

ENTRYPOINT [ "/run.sh" ]
CMD ["elasticsearch"]