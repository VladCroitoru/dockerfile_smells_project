FROM openjdk:8-jre

# system update
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install lsof procps wget curl vim less

# locale & timezone (Asia/Tokyo)
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8 \
    LANGUAGE ja_JP:ja \
    LC_ALL ja_JP.UTF-8 \
    TZ JST-9 \
    TERM xterm

# Apache Solr4
ENV SOLR_VERSION="4.7.2"
ENV SOLR_USER="solr" \
    SOLR_UID="8983" \
    SOLR_GROUP="solr" \
    SOLR_GID="8983" \
    SOLR_URL="https://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz" \
    SOLR="/usr/solr/solr-$SOLR_VERSION"

RUN wget --progress=bar:force $SOLR_URL -O /tmp/solr.tgz && \
    mkdir -p /usr/solr/ && \
    tar xzvf /tmp/solr.tgz -C /usr/solr/ && \
    rm /tmp/solr.tgz

ENV SOLR_HOME="$SOLR/server"
RUN cp -R $SOLR/example $SOLR_HOME

ENV SOLR_LOG="$SOLR/logs/solr.log"
RUN mkdir $SOLR/logs

RUN groupadd -r --gid $SOLR_GID $SOLR_GROUP && \
    useradd -r --uid $SOLR_UID --gid $SOLR_GID $SOLR_USER && \
    chown -R $SOLR_USER:$SOLR_GROUP $SOLR

WORKDIR $SOLR
EXPOSE 8983
USER $SOLR_USER
ENTRYPOINT /bin/sh -c "cd $SOLR_HOME && java -Dsolr.solr.home=multicore -jar start.jar >> $SOLR_LOG 2>&1"

