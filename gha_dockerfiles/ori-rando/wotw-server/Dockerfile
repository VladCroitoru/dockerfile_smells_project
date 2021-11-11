FROM gradle:7-jdk11 as build-jar

WORKDIR /app
COPY . /app

RUN gradle jar


FROM openjdk:11-slim

WORKDIR /app

VOLUME /app/seeds

ENV SEEDGEN_PATH=/app/seedgen/seedgen
ENV WOTW_DB_HOST=db
ENV SEED_DIR=/app/seedgen/seeds
ENV WOTW_DB=postgres
ENV WOTW_DB_PORT=5432
ENV WOTW_DB_USER=postgres

COPY --from=build-jar /app/build/libs/wotw-server.jar /app/server/wotw-server.jar
COPY --from=ghcr.io/ori-rando/wotw-seedgen /app/ /app/seedgen/
COPY ./entrypoint /app/entrypoint

RUN adduser --no-create-home --disabled-password --uid 1010 wotw && \
    chown -R wotw /app && \
    apt-get update -y && \
    apt-get install netcat -y

USER wotw

ENTRYPOINT ["/app/entrypoint"]
CMD ["java", "-jar", "/app/server/wotw-server.jar"]
