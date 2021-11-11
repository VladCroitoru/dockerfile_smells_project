FROM kartoza/geoserver:2.19.0

ADD ./plugins/gt-jdbc-hana-25.1.jar /usr/local/tomcat/webapps/geoserver/WEB-INF/lib
ADD ./plugins/ngdbc-2.8.14.jar /usr/local/tomcat/webapps/geoserver/WEB-INF/lib

# Set data_dir content for Geoserver container
COPY --chown=geoserveruser:geoserverusers data_dir /opt/geoserver/data_dir
