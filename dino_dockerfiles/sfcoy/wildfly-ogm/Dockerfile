FROM jboss/wildfly:latest

WORKDIR $JBOSS_HOME/modules

ARG MAVEN_REPO=https://repo1.maven.org/maven2

ENV ORM_VERSION 5.1.8.Final
ENV OGM_VERSION 5.1.0.Final
ENV SEARCH_VERSION 5.6.1.Final
ENV WILDFLY_VERSION wildfly-10

RUN curl -L -O $MAVEN_REPO/org/hibernate/hibernate-orm-modules/$ORM_VERSION/hibernate-orm-modules-$ORM_VERSION-$WILDFLY_VERSION-dist.zip \
     && unzip hibernate-orm-modules-$ORM_VERSION-$WILDFLY_VERSION-dist.zip \
     && rm hibernate-orm-modules-$ORM_VERSION-$WILDFLY_VERSION-dist.zip

RUN curl -L -O $MAVEN_REPO/org/hibernate/ogm/hibernate-ogm-modules/$OGM_VERSION/hibernate-ogm-modules-$OGM_VERSION-$WILDFLY_VERSION-dist.zip \
     && unzip hibernate-ogm-modules-$OGM_VERSION-$WILDFLY_VERSION-dist.zip \
     && rm hibernate-ogm-modules-$OGM_VERSION-$WILDFLY_VERSION-dist.zip

RUN curl -L -O $MAVEN_REPO/org/hibernate/hibernate-search-modules/$SEARCH_VERSION/hibernate-search-modules-$SEARCH_VERSION-$WILDFLY_VERSION-dist.zip \
     && unzip hibernate-search-modules-$SEARCH_VERSION-$WILDFLY_VERSION-dist.zip \
     && rm hibernate-search-modules-$SEARCH_VERSION-$WILDFLY_VERSION-dist.zip

WORKDIR $JBOSS_HOME

