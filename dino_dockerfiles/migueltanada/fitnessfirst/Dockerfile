FROM migueltanada/centos-java:8

MAINTAINER BATMAN

RUN mkdir -p /opt/fitnesse

WORKDIR /opt/fitnesse

EXPOSE 80

VOLUME /opt/fitnesse/

COPY Resources/. /opt/fitnesse/

RUN mkdir -p  /opt/fitnesse/FitNesseRoot

ENTRYPOINT ["/opt/fitnesse/entrypoint.sh"]
