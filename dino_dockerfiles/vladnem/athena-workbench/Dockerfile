FROM nathonfowlie/centos-jre
MAINTAINER Vlad Nemes <me@vladnem.es>

RUN yum install -y unzip && \
	mkdir /var/driver && \
	mkdir /var/workbench && \
	curl -o /var/driver/athena.jar https://s3.amazonaws.com/athena-downloads/drivers/AthenaJDBC41-1.0.0.jar && \
	curl -o /tmp/workbench.zip http://www.sql-workbench.net/Workbench-Build121.zip && \
	unzip /tmp/workbench.zip -d /var/workbench

WORKDIR /var/workbench

ENTRYPOINT ["java", \
	"-jar", "sqlworkbench.jar", \
	"-driver=com.amazonaws.athena.jdbc.AthenaDriver", \
	"-driverjar=/var/driver/athena.jar", \
	"-displayResult=true", \
	"-showTiming=true"]
