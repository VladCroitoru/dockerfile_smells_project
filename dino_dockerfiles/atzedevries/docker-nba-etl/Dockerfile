FROM openjdk:8
#FROM openjdk:8-alpine
MAINTAINER atze.devries@naturalis.nl

ENV ES_DNS=es DEFAULT_SHARDS=12 NUM_REPLICAS=0 NBA_INDEX_NAME=nba COL_YEAR=2016 PURL_BASE_URL='' 
ENV TEST_GENERA=#test_genera=malus,parus,larus,bombus,rhododendron,felix,tulipa,rosa,canis,passer,trientalis
ENV AUTO_IMPORT=FALSE GIT_URL_PREFIX=https://github.com/naturalis/ IMPORT_DATA_DIR=/payload/data IMPORT_COMMAND=./import-all CONSOLE_LOG=FALSE DISABLE_TRUNCATE=FALSE
ENV REPOS="nba-brondata-nsr:master,nba-brondata-medialib:master,nba-brondata-crs:master,nba-brondata-col:master,nba-brondata-brahms:master,nba-brondata-geo:master"
ENV FILEBEAT_VERSION=5.1.2 LOG_LEVEL=INFO ENABLE_FILEBEAT=FALSE LANG=en_US.UTF-8 PATCH_PROPERTIES=TRUE
#RUN mkdir /payload
#RUN apk add --no-cache bash git

RUN apt-get update \
    && apt-get install -y git \
    && curl -L https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz | tar -xvz \
    && mv /filebeat-${FILEBEAT_VERSION}-linux-x86_64 /filebeat \
    && mkdir -p /payload/data 

WORKDIR /payload
ADD software software
#RUN mkdir data
#ADD version /payload/software/sh/version
ADD log4j2.xml /payload/software/conf/log4j2.xml
WORKDIR /payload/software/sh
ADD run.sh run.sh
ADD etl.yml /filebeat/etl.yml
ADD version version
RUN chmod +x run.sh
CMD ./run.sh
