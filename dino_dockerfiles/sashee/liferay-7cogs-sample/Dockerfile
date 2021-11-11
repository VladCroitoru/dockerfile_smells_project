FROM ubuntu:16.04

RUN apt-get update && \
	apt-get install -y default-jdk wget unzip

RUN wget https://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.0.6/liferay-portal-tomcat-6.0.6-20110225.zip/download && \
	unzip download && \
	rm download

EXPOSE 8080

CMD ["/liferay-portal-6.0.6/tomcat-6.0.29/bin/catalina.sh", "run"]
