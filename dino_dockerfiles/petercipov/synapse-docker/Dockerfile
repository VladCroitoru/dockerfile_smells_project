FROM debian:9.4-slim
ARG SYNAPSE_VERSION=0.30.0-1
ENV MATRIX_UID=991 MATRIX_GID=991 MATRIX_GENERATE=false MATRIX_SERVER_NAME=change.me MATRIX_SEND_STATS=no

ADD https://matrix.org/packages/debian/repo-key.asc /var/matrix/repo-key.asc
ADD defaults /var/matrix/defaults
ADD run.sh /run.sh

EXPOSE 8008
EXPOSE 8448

RUN apt-get update -q && \
    apt-get install -q -y gnupg && \
    apt-key add /var/matrix/repo-key.asc

ADD matrix.list /etc/apt/sources.list.d/matrix.list

RUN cat /var/matrix/defaults | debconf-set-selections && \
    apt-get update -q && \
    apt-get install matrix-synapse=${SYNAPSE_VERSION} libpq-dev -q -y && \
    easy_install pip && \
    pip install psycopg2-binary

ENTRYPOINT ["/run.sh"]
