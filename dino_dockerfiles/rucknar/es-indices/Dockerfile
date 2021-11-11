FROM gliderlabs/alpine
MAINTAINER Ed Marshall

RUN apk-install bash curl grep

ADD elasticsearch-remove-old-indices.sh elasticsearch-remove-old-indices.sh
ADD run.sh /run.sh

RUN chmod 755 /*.sh

ENV ELASTICSEARCH_ENDPOINT **None**
ENV CLEAN_PERIOD **None**
ENV INDEX logstash*

CMD /run.sh
