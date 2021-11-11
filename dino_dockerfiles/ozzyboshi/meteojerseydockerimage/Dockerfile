
FROM tomcat:8.0

RUN apt-get update -q
RUN apt-get install -qy git
RUN apt-get install -qy openjdk-7-jre
RUN apt-get install -qy openjdk-7-jdk
ADD tomcat-users.xml /tomcat-users.xml
ADD start.sh /start.sh
RUN chmod +x /start.sh
RUN git clone https://github.com/Ozzyboshi/WeatherstationJavaWS.git /tmp/WeatherStation
RUN cp -r /tmp/WeatherStation/build/classes /tmp/WeatherStation/WebContent/WEB-INF/
RUN cd /tmp/WeatherStation/WebContent && jar -cvf $CATALINA_HOME/webapps/WeatherStation.war *
ENTRYPOINT [ "/start.sh" ]
