FROM ubuntu:16.04

ENV GERRIT_HOME /var/gerrit
ENV GERRIT_SITE ${GERRIT_HOME}/review_site
ENV GERRIT_WAR ${GERRIT_HOME}/gerrit.war
ENV GERRIT_VERSION 2.12.4
ENV GERRIT_USER gerrit

# Allow remote connectivity, sudo and git!
# Install OpenJDK and Gerrit in two subsequent transactions
# (pre-trans Gerrit script needs to have access to the Java command)
RUN apt-get update
RUN apt-get -y install openssh-client sudo git openjdk-8-jdk libcgi-pm-perl gitweb libbcprov-java libbcpkix-java

# Need to create path to etc in review site.
RUN mkdir -p $GERRIT_SITE/etc
ADD https://gerrit-releases.storage.googleapis.com/gerrit-$GERRIT_VERSION.war $GERRIT_WAR

RUN useradd -ms /bin/bash $GERRIT_USER && \
chown -R $GERRIT_USER:$GERRIT_USER $GERRIT_HOME

USER $GERRIT_USER

EXPOSE 29418 8080
VOLUME $GERRIT_SITE

WORKDIR $GERRIT_HOME
CMD java -jar $GERRIT_WAR init \
--batch \
--no-auto-start \
-d $GERRIT_SITE \
--install-plugin singleusergroup \
--install-plugin download-commands \
--install-plugin replication \
--install-plugin reviewnotes \
--install-plugin commit-message-length-validator && \
java -jar $GERRIT_WAR reindex -d $GERRIT_SITE && \
 $GERRIT_SITE/bin/gerrit.sh start && \
 tail -f $GERRIT_SITE/logs/error_log
