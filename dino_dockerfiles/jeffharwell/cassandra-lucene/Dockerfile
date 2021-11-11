#FROM launcher.gcr.io/google/cassandra3:3.11
FROM gcr.io/cloud-marketplace-containers/google/cassandra3:3.11
MAINTAINER Jeff Harwell <jeff.harwell@gmail.com>

## This is, of course, non-ideal.
## If I had the dockerfile for the GCR image I would do this differently

## Download and install the Lucene Index plugin. The compiled binary is at www.jeffharwell.com
COPY ./ready-probe.sh /
RUN chmod +x /ready-probe.sh && \
    gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv E91335D77E3E87CB && \
    gpg --export --armor E91335D77E3E87CB | apt-key add - && \
    apt-get -y update && \
    apt-get -y -o Dpkg::Options::="--force-confold" upgrade cassandra && \
    apt-get -y upgrade && \
    apt-get -y install wget && \
    wget http://www.jeffharwell.com/jars/cassandra-lucene-index-plugin-3.11.1.0.jar && \
    mv ./cassandra-lucene-index-plugin-3.11.1.0.jar /usr/share/cassandra/lib/ && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

## There definitely a better way to do this, but we are going to go ahead 
## and hard code the G1 garbage collector as per:
## https://docs.datastax.com/en/archived/cassandra/3.x/cassandra/operations/opsTuneJVM.html
COPY ./jvm.options /etc/cassandra/
