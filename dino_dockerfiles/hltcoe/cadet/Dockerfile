FROM maven as builder
WORKDIR /build
COPY . /build
RUN mvn -B clean package -DskipTests=true
RUN mv `find cadet-ui/target -name "cadet-ui-*.war"` cadet-ui.war

FROM tomcat:7-jre8
RUN rm -rf /usr/local/tomcat/webapps/ROOT
COPY --from=builder /build/cadet-ui.war /usr/local/tomcat/webapps/
COPY docker-conf/server.xml /usr/local/tomcat/conf/
COPY docker-conf/tomcat-users.xml /usr/local/tomcat/conf/
