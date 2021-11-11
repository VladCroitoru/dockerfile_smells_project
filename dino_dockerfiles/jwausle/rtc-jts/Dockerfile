FROM ubuntu

MAINTAINER jwausle

WORKDIR /  
COPY . /rtc-server
RUN mkdir -p /rtc-server/server/tomcat/logs && \
    touch /rtc-server/server/tomcat/logs/catalina.out

EXPOSE 9443 9080 9009
VOLUME /rtc-server

CMD /rtc-server/server/server.startup & tailf rtc-server/server/tomcat/logs/catalina.out 


