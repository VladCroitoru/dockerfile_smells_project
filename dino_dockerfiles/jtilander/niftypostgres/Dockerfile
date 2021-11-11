FROM postgres:9.6
MAINTAINER jim@tilander.org

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -yq --no-install-recommends dos2unix && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD *.sh /docker-entrypoint-initdb.d/
RUN chmod a+x /docker-entrypoint-initdb.d/*.sh
RUN dos2unix /docker-entrypoint-initdb.d/*.sh
