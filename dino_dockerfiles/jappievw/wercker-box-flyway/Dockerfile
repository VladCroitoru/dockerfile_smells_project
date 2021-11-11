FROM jappievw/wercker-box-base:1

LABEL org.label-schema.name="wercker-box-flyway" \
      org.label-schema.description="Debian based box with some extras for Wercker pipelines to use Flyway." \
      org.label-schema.url="https://github.com/jappievw/wercker-box-flyway" \
      org.label-schema.org.vcs-url="https://github.com/jappievw/wercker-box-flyway" \
      org.label-schema.org.vcs-type="git" \
      org.label-schema.schema-version="1.0"

ARG FLYWAY_VERSION=4.0.3

RUN mkdir -p /opt/flyway \
    && curl -L https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}-linux-x64.tar.gz -o flyway-commandline-${FLYWAY_VERSION}.tar.gz \
    && tar -xzf flyway-commandline-${FLYWAY_VERSION}.tar.gz --strip-components=1 -C /opt/flyway \
    && rm flyway-commandline-${FLYWAY_VERSION}.tar.gz

ENV PATH /opt/flyway:$PATH
