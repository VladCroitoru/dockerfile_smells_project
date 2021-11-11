FROM frolvlad/alpine-oraclejdk8:latest

LABEL maintainer="victor.perticarrari@gmail.com"

ADD https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/4.2.0/flyway-commandline-4.2.0.tar.gz flyway-commandline-4.2.0.tar.gz

RUN tar -xvzf flyway-commandline-4.2.0.tar.gz
RUN rm flyway-commandline-4.2.0.tar.gz
RUN mv flyway-4.2.0 flyway

RUN apk --update add bash

WORKDIR /flyway

ADD migrate.sh /flyway/migrate.sh

ENTRYPOINT ["/flyway/migrate.sh"]
