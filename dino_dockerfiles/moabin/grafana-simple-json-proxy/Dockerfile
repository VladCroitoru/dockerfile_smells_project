FROM dchq/tomcat
MAINTAINER moabin <moabin@gmail.com>



ENV VERSION 1.0
ENV WAR grafana-simple-json-proxy-$VERSION.war

RUN mkdir -p /opt/jmx_exporter
RUN curl -L https://github.com/moabin/grafana-simple-json-proxy/raw/master/target/$WAR -o /usr/local/tomcat/webapps/grafana-simple-json-proxy.war
