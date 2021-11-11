FROM postgres:11.6

MAINTAINER Tomas Jelen <tomas@delikates.org>

RUN apt-get update && apt-get install -y curl

RUN curl https://postgres.cz/data/czech.tar.gz \
  | tar -xzC /tmp/ \
  && mv /tmp/fulltext_dicts/czech.* /usr/share/postgresql/11/tsearch_data/

ADD add-tsearch-czech.sh docker-entrypoint-initdb.d/
