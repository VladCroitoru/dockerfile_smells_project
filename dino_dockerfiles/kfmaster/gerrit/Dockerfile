# Based on openfrontier/gerrit, slightly modified by kfmaster
# Original MAINTAINER zsx <thinkernel@gmail.com>

FROM library/java:openjdk-7-jre

MAINTAINER kfmaster <fuhaiou@hotmail.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    libcgi-pm-perl \
    gitweb \
  && rm -rf /var/lib/apt/lists/*

ENV GERRIT_HOME /var/gerrit
ENV GERRIT_SITE ${GERRIT_HOME}/review_site
ENV GERRIT_WAR ${GERRIT_HOME}/gerrit.war
ENV GERRIT_VERSION 2.10.3.1
ENV GERRIT_USER gerrit2

COPY gerrit-entrypoint.sh ${GERRIT_HOME}/
COPY gerrit-start.sh ${GERRIT_HOME}/

#Download gerrit.war
RUN useradd -m -d "$GERRIT_HOME" -u 1000 -U  -s /bin/bash $GERRIT_USER \
   && chmod +x ${GERRIT_HOME}/gerrit*.sh \
   && mkdir -p $GERRIT_SITE
   
#RUN curl -sL https://gerrit-releases.storage.googleapis.com/gerrit-${GERRIT_VERSION}.war -o $GERRIT_WAR 
#To workaround download problem
COPY gerrit.war $GERRIT_WAR

USER $GERRIT_USER

#Gerrit site directory is a volume, so configuration and repositories
#can be persisted and survive image upgrades.

VOLUME $GERRIT_SITE

EXPOSE 8080 29418

ENTRYPOINT ["/var/gerrit/gerrit-entrypoint.sh"]

CMD ["/var/gerrit/gerrit-start.sh"]

