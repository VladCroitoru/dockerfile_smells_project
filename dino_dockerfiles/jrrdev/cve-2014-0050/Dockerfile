FROM maven:3-jdk-8-alpine

MAINTAINER jrrdev

RUN mkdir -p /cve-2014-0050/exploit && \
	mkdir -p /usr/src/cve-2014-0050

ADD ./pom.xml /usr/src/cve-2014-0050/pom.xml
ADD ./src /usr/src/cve-2014-0050/src
ADD ./docker/entry-point.sh /cve-2014-0050/entry-point.sh
ADD ./exploit/exploit.py /cve-2014-0050/exploit/exploit.py


RUN chmod +x /cve-2014-0050/entry-point.sh && \
	sync && \
	cd /usr/src/cve-2014-0050 && \
	mvn package && \
	cp /usr/src/cve-2014-0050/target/*.jar /cve-2014-0050/cve-2014-0050-example.jar && \
	rm -Rf /usr/src/cve-2014-0050

WORKDIR /cve-2014-0050

ENTRYPOINT ["./entry-point.sh"]

EXPOSE 8080

VOLUME ["/cve-2014-0050/exploit/"]
