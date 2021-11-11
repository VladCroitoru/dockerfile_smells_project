FROM davidcaste/alpine-tomcat:tomcat8
ARG VERSION=2.4
ARG OBF_SUFFIX=""
LABEL maintainer="sebastianrevuelta@gmail.com"
LABEL name="chess vulnerable game"
COPY build/libs/chess-${VERSION}${OBF_SUFFIX}.war /opt/tomcat/webapps/chess.war
ADD /logs/chess.log /opt/tomcat/logs/chess.log
EXPOSE 8080
CMD ["/opt/tomcat/bin/catalina.sh", "run"]
