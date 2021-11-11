FROM driveclutch/alpine-java:2.2

USER root

RUN apt-get update && apt-get install -y --no-install-recommends && \
    apt-get install -y "postgresql-client-11"

COPY lib/* /tmp/

RUN mkdir liquibase && \
    tar -xzf /tmp/liquibase-3.5.3-bin.tar.gz -C liquibase && \
    chmod +x liquibase/liquibase && \
    mkdir jdbc_drivers && \
    mv /tmp/postgresql-42.1.4.jar jdbc_drivers && \
    mkdir migrations

WORKDIR migrations

COPY bin/ecs-set-desired /app/ecs-set-desired

COPY update.sh /app
COPY shutdown.sh /app

CMD bash /app/update.sh
