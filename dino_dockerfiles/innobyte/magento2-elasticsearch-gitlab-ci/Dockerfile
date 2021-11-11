FROM elasticsearch:2.4.5
MAINTAINER Alin Alexandru <alin.alexandru@innobyte.com>

# Install elasticsearch 2.4. Needed by https://github.com/Smile-SA/elasticsuite

RUN /usr/share/elasticsearch/bin/plugin install analysis-phonetic
RUN /usr/share/elasticsearch/bin/plugin install analysis-icu

COPY config ./config
