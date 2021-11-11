FROM openjdk:8-jre-alpine

ENV 	V=5.15.0	\
	HAWTIO=1.5.2

RUN apk --no-cache add openssl

RUN wget -O apache-activemq-${V}-bin.tar.gz  											\
	 "http://www.apache.org/dyn/closer.cgi?filename=/activemq/${V}/apache-activemq-${V}-bin.tar.gz&action=download" &&  	\
    tar xvp -C /srv -f  apache-activemq-${V}-bin.tar.gz && \
    rm apache-activemq-${V}-bin.tar.gz

RUN mkdir -p /srv/activemq && \
    mv /srv/apache-activemq-*/conf /srv/activemq && \
    mv /srv/apache-activemq-*/data /srv/activemq

RUN mkdir /srv/hawtio						\
 && wget -O /srv/hawtio/hawtio-default-offline-${HAWTIO}.war	\
	"https://oss.sonatype.org/content/repositories/public/io/hawt/hawtio-default-offline/${HAWTIO}/hawtio-default-offline-${HAWTIO}.war"	\
 && ln -s hawtio-default-offline-${HAWTIO}.war /srv/hawtio/hawtio-default-offline.war

RUN echo "" >> "/srv/apache-activemq-${V}/bin/env"	\
 && echo 'ACTIVEMQ_OPTS="$ACTIVEMQ_OPTS -Dhawtio.realm=activemq -Dhawtio.role=admins -Dhawtio.rolePrincipalClasses=org.apache.activemq.jaas.GroupPrincipal"'	\
	>> "/srv/apache-activemq-${V}/bin/env"

RUN echo 'ACTIVEMQ_OPTS="$ACTIVEMQ_OPTS -Dcom.sun.management.jmxremote.port=1099 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"'	>> "/srv/apache-activemq-${V}/bin/env"

COPY networkrail.xml  /srv/activemq/conf/networkrail.xml.template
COPY nationalrail.xml /srv/activemq/conf/nationalrail.xml.template
COPY streamcache.xml  /srv/activemq/conf/streamcache.xml
COPY localbroker.xml  /srv/activemq/conf/localbroker.xml
COPY init.sh /
RUN chmod +x /init.sh

ENV NETWORKRAIL_USERNAME= NETWORKRAIL_PASSWORD= NETWORKRAIL_TOPICS=
ENV NATIONALRAIL_USERNAME=d3user NATIONALRAIL_PASSWORD=d3password NATIONALRAIL_QUEUE=

VOLUME /srv/activemq/data

EXPOSE 1099 5672 8161 1883 61613 61614 61616

CMD ["/init.sh"]

