# version 0.1
FROM ubuntu:16.04
MAINTAINER Celso "xxxx@xxxxx.com"
RUN apt-get update; apt-get install -y unzip curl nano

# add webupd8 repository
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean

RUN curl http://download.jboss.org/wildfly/10.0.0.Final/wildfly-10.0.0.Final.zip -o wildfly-10.0.0.Final.zip
RUN curl http://downloads.jboss.org/apiman/1.2.8.Final/apiman-distro-wildfly10-1.2.8.Final-overlay.zip -o apiman-distro-wildfly10-1.2.8.Final-overlay.zip
RUN unzip wildfly-10.0.0.Final.zip
RUN unzip -o apiman-distro-wildfly10-1.2.8.Final-overlay.zip -d wildfly-10.0.0.Final
RUN rm wildfly-10.0.0.Final.zip; rm apiman-distro-wildfly10-1.2.8.Final-overlay.zip
CMD cd wildfly-10.0.0.Final && ./bin/standalone.sh -b 0.0.0.0 -bmanagement 0.0.0.0 -c standalone-apiman.xml 
EXPOSE 8080
