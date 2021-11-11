FROM alpine

#
# Build: docker build --force-rm --rm=true -t gustajz/liquibase .
#

MAINTAINER Gustavo Jotz

RUN apk add --update bash tzdata curl openjdk8-jre && rm -rf /var/cache/apk/*

ENV TZ America/Sao_Paulo
ENV PATH $PATH:/liquibase

ENV LIQUIBASE_VERSION 3.5.1

RUN mkdir -p /liquibase && \
    curl -L https://github.com/liquibase/liquibase/releases/download/liquibase-parent-${LIQUIBASE_VERSION}/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz | tar xzC /liquibase
    
RUN curl -L -o /liquibase/lib/postgresql-9.4.1208.jar https://jdbc.postgresql.org/download/postgresql-9.4.1208.jar

CMD ["liquibase", "--version"]
