FROM debian:jessie

MAINTAINER Rurik Thomas Greenall <rurik.greenall@computas.com>

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get install -y tar locales git openjdk-7-jre-headless maven

RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8
ENV LC_ALL C.UTF-8


RUN mkdir /working && cd /working && git clone https://github.com/apache/jena.git
RUN cd /working/jena/jena-fuseki2/jena-fuseki-dist/ && mvn clean install 
RUN mkdir /opt/fuseki2

RUN tar -zxvf /working/jena/jena-fuseki2/jena-fuseki-dist/target/jena-fuseki-dist-2.0.0-SNAPSHOT.tar.gz -C /opt/fuseki2

RUN chmod +x /opt/fuseki2/jena-fuseki-dist-2.0.0-SNAPSHOT/fuseki-server

RUN rm -R /working

ADD startup.sh /opt/fuseki2/jena-fuseki-dist-2.0.0-SNAPSHOT/startup.sh
RUN chmod +x /opt/fuseki2/jena-fuseki-dist-2.0.0-SNAPSHOT/startup.sh

RUN mkdir /data
VOLUME /data
EXPOSE 3030
CMD ["/opt/fuseki2/jena-fuseki-dist-2.0.0-SNAPSHOT/startup.sh"]