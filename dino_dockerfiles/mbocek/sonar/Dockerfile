FROM dockerfile/java
MAINTAINER  Michal Bocek <michal.bocek@gmail.com>

RUN echo "deb http://downloads.sourceforge.net/project/sonar-pkg/deb binary/" >> /etc/apt/sources.list
RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y --force-yes sonar

RUN sed -i 's|#wrapper.java.additional.6=-server|wrapper.java.additional.6=-server|g' /opt/sonar/conf/wrapper.conf

RUN sed -i 's|#sonar.jdbc.password=sonar|sonar.jdbc.password=${env:SONAR_PASSWORD}|g' /opt/sonar/conf/sonar.properties
RUN sed -i 's|#sonar.jdbc.user=sonar|sonar.jdbc.user=${env:SONAR_USER}|g' /opt/sonar/conf/sonar.properties
RUN sed -i 's|sonar.jdbc.url=jdbc:h2|#sonar.jdbc.url=jdbc:h2|g' /opt/sonar/conf/sonar.properties
RUN sed -i 's|#sonar.jdbc.url=jdbc:mysql://localhost|sonar.jdbc.url=jdbc:mysql://${env:SONAR_HOST}|g' /opt/sonar/conf/sonar.properties 
RUN sed -i 's|#sonar.web.context=|sonar.web.context=${env:SONAR_CONTEXT}|g' /opt/sonar/conf/sonar.properties 

EXPOSE 9000

CMD ["/opt/sonar/bin/linux-x86-64/sonar.sh","console"]