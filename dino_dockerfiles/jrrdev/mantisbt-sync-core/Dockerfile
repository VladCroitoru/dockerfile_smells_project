FROM maven:3-jdk-8-alpine

MAINTAINER jrrdev

RUN mkdir -p /mantis-sync-core && \
	mkdir -p /usr/src/mantis-sync-core


ADD ./pom.xml /usr/src/mantis-sync-core/pom.xml
ADD ./src /usr/src/mantis-sync-core/src
ADD ./docker/entry-point.sh /mantis-sync-core/entry-point.sh

RUN chmod +x /mantis-sync-core/entry-point.sh && \
	sync && \
	cd /usr/src/mantis-sync-core && \
	mvn package && \
	cp /usr/src/mantis-sync-core/target/*.jar /mantis-sync-core/mantis-sync-core.jar && \
	rm -Rf /usr/src/mantis-sync-core

WORKDIR /mantis-sync-core

ENV SPRING_PROFILES_ACTIVE prod

ENTRYPOINT ["./entry-point.sh"]

EXPOSE 8080

VOLUME ["/shared/data"]


