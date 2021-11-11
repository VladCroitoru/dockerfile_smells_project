FROM maven:3-jdk-8-alpine

MAINTAINER jrrdev

RUN mkdir -p /mantis-sync-REST && \
	mkdir -p /usr/src/mantis-sync-REST

ADD ./pom.xml /usr/src/mantis-sync-REST/pom.xml
ADD ./src /usr/src/mantis-sync-REST/src
ADD ./docker/entry-point.sh /mantis-sync-REST/entry-point.sh


RUN chmod +x /mantis-sync-REST/entry-point.sh && \
	sync && \
	cd /usr/src/mantis-sync-REST && \
	mvn package && \
	cp /usr/src/mantis-sync-REST/target/*.jar /mantis-sync-REST/mantisbt-sync-REST.jar && \
	rm -Rf /usr/src/mantis-sync-REST

WORKDIR /mantis-sync-REST

ENTRYPOINT ["./entry-point.sh"]

EXPOSE 8080
