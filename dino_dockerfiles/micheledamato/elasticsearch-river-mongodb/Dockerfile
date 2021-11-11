FROM elasticsearch:1.4.5
MAINTAINER "Michele D'Amato"

RUN /usr/share/elasticsearch/bin/plugin --install com.github.richardwilly98.elasticsearch/elasticsearch-river-mongodb/2.0.9

CMD ["elasticsearch","restart"]
