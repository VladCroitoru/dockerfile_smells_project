FROM gliderlabs/alpine:3.2

ENV CURATOR_VERSION 5.5.4
#ENV ELASTICSEARCH_PORT 9200
#ENV MAX_INDEX_AGE 0
#ENV ELASTICSEARCH_HOST elasticsearch

RUN apk --update add python py-pip bash && pip install --upgrade  elasticsearch-curator==$CURATOR_VERSION

ADD docker-entrypoint.sh /
ADD tasks/optimize-indices.sh /etc/periodic/
ADD tasks/purge-old-indices.sh /etc/periodic/

RUN chmod +x /docker-entrypoint.sh
RUN chmod +x /etc/periodic/purge-old-indices.sh
RUN chmod +x /etc/periodic/optimize-indices.sh

RUN printf "\n*/5\t*\t*\t*\t*\t/etc/periodic/purge-old-indices.sh" >> /etc/crontabs/root
RUN printf "\n*/5\t*\t*\t*\t*\t/etc/periodic/optimize-indices.sh" >> /etc/crontabs/root

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["crond", "-f", "-l", "8"]
