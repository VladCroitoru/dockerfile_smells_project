FROM solr

MAINTAINER Allen Day "allenday@allenday.com"

USER root
WORKDIR /

ENV BUILD_PACKAGES=""
ENV IMAGE_PACKAGES="git maven telnet openjdk-8-jdk"

RUN apt-get -y update
RUN apt-get -y --no-install-recommends install $BUILD_PACKAGES $IMAGE_PACKAGES

#tomcat http
EXPOSE 9999
#solr  http
EXPOSE 8983

## cleanup
#RUN apt-get -y remove --purge $BUILD_PACKAGES
#RUN apt-get -y remove --purge $(apt-mark showauto)
#RUN rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/allenday/image-similarity.git
RUN cd image-similarity && mvn install assembly:single -DskipTests

COPY entrypoint.sh /entrypoint.sh
COPY uploadservlet /uploadservlet
RUN cd /uploadservlet && mvn package
#RUN mkdir -p /opt/solr/server/solr/frameshift/conf
#COPY solr-data /solr-data
#COPY solr-data-full /solr-data-full

USER solr
WORKDIR /tmp

RUN solr start && sleep 5 && solr create_core -c frameshift -p 8983 && solr stop -p 8983
#$-d /opt/solr/server/solr/frameshift 
#$COPY managed-schema /opt/solr/server/solr/frameshift/conf/managed-schema
#ADD solr-data /var/solr/data

ENTRYPOINT ["/bin/bash","/entrypoint.sh"]

