FROM elasticsearch:5.5
MAINTAINER Ali Ghassabian <ghasabian@hotmail.com>

RUN bin/elasticsearch-plugin install x-pack
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
