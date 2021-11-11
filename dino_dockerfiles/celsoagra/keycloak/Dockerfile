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

RUN curl https://downloads.jboss.org/keycloak/3.0.0.Final/keycloak-3.0.0.Final.zip -o keycloak-3.0.0.Final.zip
RUN unzip keycloak-3.0.0.Final.zip
RUN rm keycloak-3.0.0.Final.zip
RUN ./keycloak-3.0.0.Final/bin/add-user-keycloak.sh -u admin -p admin
CMD cd keycloak-3.0.0.Final && ./bin/standalone.sh -b 0.0.0.0 -bmanagement 0.0.0.0 -c standalone.xml 
EXPOSE 8080
