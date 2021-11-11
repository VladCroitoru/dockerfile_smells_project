FROM tomcat:9-jre8-alpine

MAINTAINER yohayg@gmail.com

RUN apk update && apk add sed
##build image
#docker build -t yohayg/tomcat-deployment-listener:3.0.0 .

##run container
#docker run -it --rm -p 8080:8080  yohayg/tomcat-deployment-listener:3.0.0

#add the listener to the tomcat server.xml
#pretty print with \t and \n
RUN sed -i \
    's/<\/Server>/\\t<Listener className="org.apache.tomcat.deployment.listener.StrictStateCheckListener" \/>\\n<\/Server>/g' \
    $CATALINA_HOME/conf/server.xml \
    && awk '{gsub("\\\\n","\n")};1'  $CATALINA_HOME/conf/server.xml > $CATALINA_HOME/conf/server_temp.xml \
    && mv $CATALINA_HOME/conf/server_temp.xml $CATALINA_HOME/conf/server.xml \
    && awk '{gsub("\\\\t","\t")};1'  $CATALINA_HOME/conf/server.xml > $CATALINA_HOME/conf/server_temp.xml \
    && mv $CATALINA_HOME/conf/server_temp.xml $CATALINA_HOME/conf/server.xml

#add the jar to tomcat lib
COPY target/tomcat-deployment-listener-3.0.0-SNAPSHOT.jar $CATALINA_HOME/lib

EXPOSE 8080
CMD ["catalina.sh", "run"]
