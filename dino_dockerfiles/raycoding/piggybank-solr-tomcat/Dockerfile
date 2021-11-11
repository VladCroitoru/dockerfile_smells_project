FROM raycoding/piggybank
MAINTAINER Shuddhashil Ray rayshuddhashil@gmail.com

# Environment Variables
ENV SOLR_VERSION 4.8.1
ENV TOMCAT_VERSION 7.0.32
ENV SOLR solr-$SOLR_VERSION
ENV TOMCAT apache-tomcat-$TOMCAT_VERSION
ENV SOLR_HOME /usr/lib/solr-home
ENV TOMCAT_HOME /usr/lib/$TOMCAT
ENV SOLR_ZK_CLI /usr/lib/solr-zk-cli

# Fetch Apache Tomcat 7.0.32
RUN (cd /usr/lib/ && wget -q -nc http://archive.apache.org/dist/tomcat/tomcat-7/v$TOMCAT_VERSION/bin/$TOMCAT.zip)
RUN unzip -q /usr/lib/$TOMCAT.zip -d /usr/lib

# Fetch Solr 4.8.1
RUN (cd /usr/lib && wget -q -nc http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.zip)
RUN unzip -q /usr/lib/$SOLR.zip -d /usr/lib

#Setting up Apache 7.0.32 with Solr 4.8.1
RUN cp /usr/lib/$SOLR/dist/$SOLR.war /usr/lib/$TOMCAT/webapps/solr.war
RUN cp /usr/lib/$SOLR/example/lib/ext/* /usr/lib/$TOMCAT/lib/
RUN mkdir -p $SOLR_HOME

ADD apache_tomcat_setenv.sh /usr/lib/$TOMCAT/bin/setenv.sh
ADD tomcat-users.xml /usr/lib/$TOMCAT/conf/tomcat-users.xml
RUN sed -i s/8080/8983/g /usr/lib/$TOMCAT/conf/server.xml
ADD solr.xml $SOLR_HOME/solr.xml

#Setting Up ZooKeeper Command Line Interface provided by Solr
RUN mkdir -p $SOLR_ZK_CLI
RUN unzip -q /usr/lib/$SOLR/dist/$SOLR.war -d /tmp/solr-war
RUN cp  /tmp/solr-war/WEB-INF/lib/* $SOLR_ZK_CLI
RUN cp /usr/lib/$SOLR/example/lib/ext/* $SOLR_ZK_CLI
RUN rm -rf /tmp/solr-war

#Setting Up Symlinks
RUN ln -s $SOLR_HOME /solr-home
RUN ln -s $TOMCAT_HOME /tomcat-home
RUN ln -s /usr/lib/$SOLR /solr-dist
RUN ln -s $SOLR_ZK_CLI /solr-zk-cli

RUN chmod 755 -R $SOLR_HOME
RUN chmod +x /usr/lib/$TOMCAT/bin/*.sh
EXPOSE 8983

RUN rm -f /usr/lib/$SOLR.zip && rm -rf /usr/lib/$TOMCAT.zip