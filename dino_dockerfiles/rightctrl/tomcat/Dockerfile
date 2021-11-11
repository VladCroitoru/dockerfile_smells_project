FROM rightctrl/java:8
MAINTAINER RightCtrl <support@RightCtrl.com>


ENV CATALINA_HOME /opt/tomcat
ENV PATH $PATH:$CATALINA_HOME/bin:$CATALINA_HOME/scripts


# Install Tomcat
#RUN wget http://192.168.11.109/sw/apache/tomcat/apache-tomcat-8.0.36.tar.gz && \
#RUN wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.36/bin/apache-tomcat-8.0.36.tar.gz && \
RUN wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.38/bin/apache-tomcat-8.0.38.tar.gz && \
        tar -xvf apache-tomcat-8.0.38.tar.gz && \
        rm apache-tomcat*.tar.gz && \
        mv apache-tomcat* ${CATALINA_HOME}
COPY server.xml ${CATALINA_HOME}/conf/server.xml
RUN chmod +x ${CATALINA_HOME}/bin/*sh
#RUN cp -r ${CATALINA_HOME}/webapps /tmp/webapps
#RUN rm -rf ${CATALINA_HOME}/webapps/*

#ENV TZ=Asia/Tokyo
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN yum -y install epel-release


RUN printf "\n\
java.util.logging.FileHandler.level = FINE \n\
java.util.logging.FileHandler.formatter = java.util.logging.SimpleFormatter \n\
java.util.logging.FileHandler.pattern = ${CATALINA_HOME}/logs/catalina.%g.log \n\
java.util.logging.FileHandler.limit = 10000 \n\
java.util.logging.FileHandler.count = 15 \n\
\n" \
 >> ${CATALINA_HOME}/conf/logging.properties

RUN sed -i \
        -e 's/^handlers = .*/handlers = java.util.logging.FileHandler, 1catalina.org.apache.juli.AsyncFileHandler, 2localhost.org.apache.juli.AsyncFileHandler, 3manager.org.apache.juli.AsyncFileHandler, 4host-manager.org.apache.juli.AsyncFileHandler, java.util.logging.ConsoleHandler/1' \
        ${CATALINA_HOME}/conf/logging.properties

RUN yum -y install pwgen

#COPY resolv.conf /resolv.conf
#RUN printf "cp -rf /resolv.conf /etc/resolv.conf" >> /etc/rc.local
#RUN chmod +x /etc/rc.local
#
#
#CMD ["/etc/rc.local"]
#EXPOSE 8080
#CMD ["catalina.sh", "run"]

# Add the startup script
ADD run.sh /run.sh
RUN chmod +x /run.sh

# Environmental variables.
ENV ADMIN_PASS ""
ENV CERT_PASS ""
# Expose Tomcat ports
EXPOSE 8080 8443

#VOLUME ["/opt/tomcat/logs", "/opt/tomcat/work", "/opt/tomcat/webapps"]

CMD ["/run.sh"]
