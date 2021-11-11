FROM clojure:lein-2.6.1-alpine

# Based on https://hub.docker.com/r/pointslope/datomic-console/~/dockerfile/

MAINTAINER Christian Johansen "christian@kodemaker.no"

ENV DATOMIC_VERSION 0.9.5661
ENV DATOMIC_HOME /opt/datomic-pro-$DATOMIC_VERSION

RUN apk add --no-cache unzip curl

ONBUILD ADD .credentials /tmp/.credentials
ONBUILD RUN curl -u $(cat /tmp/.credentials) -SL https://my.datomic.com/repo/com/datomic/datomic-pro/$DATOMIC_VERSION/datomic-pro-$DATOMIC_VERSION.zip -o /tmp/datomic.zip \
  && unzip /tmp/datomic.zip -d /opt \
  && rm -f /tmp/datomic.zip

WORKDIR $DATOMIC_HOME

# Provide a CMD with an alias to the database and the database uri
# e.g. CMD ["dev", "datomic:dev://db:4334/"]
ENTRYPOINT ["bin/rest", "-p", "8001"]

EXPOSE 8001
