FROM jeanblanchard/busybox-java:8

# install liferay
RUN curl -O -s -k -L -C - http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.2.1%20GA2/liferay-portal-tomcat-6.2-ce-ga2-20140319114139101.zip \
    && unzip liferay-portal-tomcat-6.2-ce-ga2-20140319114139101.zip -d /opt \
    && rm liferay-portal-tomcat-6.2-ce-ga2-20140319114139101.zip \
    && mv /opt/liferay-portal-6.2-ce-ga2 /opt/liferay

# add configuration liferay file
ADD conf/portal-bundle.properties /opt/liferay/portal-bundle.properties
ADD conf/logging.properties /opt/liferay/tomcat-7.0.42/conf/logging.properties
RUN echo -e 'JAVA_OPTS="$JAVA_OPTS -Dliferay.home=/var/liferay/"' >> /opt/liferay/tomcat-7.0.42/bin/setenv.sh

# volumes
VOLUME ["/var/liferay", "/opt/liferay/"]

# Ports
EXPOSE 8080

# EXEC
CMD ["run"]
ENTRYPOINT ["/opt/liferay/tomcat-7.0.42/bin/catalina.sh"]

