FROM tomcat:8-jdk11-openjdk
COPY ./build/libs/projet-0.1.war ${CATALINA_HOME}/webapps/isitech.war
WORKDIR  /usr/local/tomcat/webapps.dist
RUN cp -r docs ../webapps && cp -r examples ../webapps && cp -r host-manager ../webapps && cp -r manager ../webapps && cp -r ROOT ../webapps
CMD ["catalina.sh" , "run"]
