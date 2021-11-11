FROM tomcat:latest
MAINTAINER martin scharm

COPY src /srv/src
COPY pom.xml /srv/pom.xml
COPY src/main/docker/M2CAT-example-context.xml /usr/local/tomcat/conf/Catalina/localhost/ROOT.xml
WORKDIR /srv/

# install dependencies, compile the code, and get rid of dependencies...
RUN apt-get update \
	&& apt-get install -y --no-install-recommends maven \
	&& mvn package \
	&& cp target/*war /usr/local/tomcat/webapps/ROOT.war \
	&& mvn clean \
	&& rm -rf /usr/local/tomcat/webapps/ROOT \
	&& rm -rf /root/.m2 /usr/share/doc \
	&& apt-get purge -y --auto-remove $deps \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*


