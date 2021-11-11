FROM tomcat:7.0.85-jre7-alpine

WORKDIR /usr/local/tomcat
COPY web.xml /usr/local/tomcat/webapps/manager/WEB-INF/
COPY startup.sh /usr/local/tomcat/bin/
COPY catalina.sh /usr/local/tomcat/bin/
COPY tomcat-users.xml /usr/local/tomcat/conf/

ENV JPDA_ADDRESS="8000"
ENV JPDA_TRANSPORT="dt_socket"

EXPOSE 8080 8443 8000

RUN mkdir -p /root/arquivos

CMD ["catalina.sh", "jpda", "run"]
