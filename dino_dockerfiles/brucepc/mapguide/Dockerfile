FROM ubuntu:14.04

# This is where mginstallubuntu.sh downloads packages into
ENV TEMPDIR /tmp/install_mapguide
ENV URL_HOST "https://download.osgeo.org"
ENV URL_RELPATH "/mapguide/releases"
ENV FDOVER_MAJOR=4
ENV FDOVER_MINOR=1
ENV FDOVER_MAJOR_MINOR=${FDOVER_MAJOR}.${FDOVER_MINOR}
ENV FDOVER_POINT=0
ENV FDOVER_MAJOR_MINOR_REV=${FDOVER_MAJOR_MINOR}.${FDOVER_POINT}
ENV FDOBUILD=7814
ENV FDOARCH=amd64
ENV FDOVER=${FDOVER_MAJOR_MINOR_REV}-${FDOBUILD}_${FDOARCH}
ENV MGVER_MAJOR=3
ENV MGVER_MINOR=1
ENV MGVER_MAJOR_MINOR=${MGVER_MAJOR}.${MGVER_MINOR}
ENV MGVER_POINT=2
ENV MGVER_MAJOR_MINOR_REV=${MGVER_MAJOR_MINOR}.${MGVER_POINT}
ENV MGRELEASELABEL=Final
ENV MGBUILD=9484
ENV MGARCH=amd64
ENV MGVER=${MGVER_MAJOR_MINOR_REV}-${MGBUILD}_${MGARCH}
ENV MG_PATH=/usr/local/mapguideopensource-${MGVER_MAJOR_MINOR_REV}
ENV MGLOG_PATH=${MG_PATH}/server/Logs
ENV MGAPACHE_LOG=${MG_PATH}/webserverextensions/apache2/logs
ENV MGTOMCAT_LOG=${MG_PATH}/webserverextensions/tomcat/logs

ENV URL_ROOT "${URL_HOST}/${URL_RELPATH}/${MGVER_MAJOR_MINOR_REV}/${MGRELEASELABEL}"
ENV URL_PART ubuntu14_x64
ENV URL "$URL_ROOT/$URL_PART"

ENV DEFAULT_SERVER_IP "0.0.0.0"
ENV DEFAULT_ADMIN_PORT 2810
ENV DEFAULT_CLIENT_PORT 2811
ENV DEFAULT_SITE_PORT 2812
ENV DEFAULT_HTTPD_PORT 8008
# ENV DEFAULT_TOMCAT_PORT 8009

RUN mkdir -p ${TEMPDIR}
WORKDIR ${TEMPDIR}

# RUN INSTALLER SCRIPT IN HEADLESS MODE
RUN apt-get update \
 && apt-get -y install wget \
 && wget ${URL}/mginstallubuntu.sh \
 && chmod +x mginstallubuntu.sh \
 && ./mginstallubuntu.sh --headless --no-service-install --no-mgserver-start \
 --no-tomcat-start --no-httpd-start --with-sdf --with-shp --with-sqlite --with-gdal \
 --with-ogr --with-wfs --admin-port ${DEFAULT_ADMIN_PORT} --client-port ${DEFAULT_CLIENT_PORT} \
 --site-port ${DEFAULT_SITE_PORT} --httpd-port ${DEFAULT_HTTPD_PORT} --server-ip ${DEFAULT_SERVER_IP} \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /var/lib/apt/archives/*

WORKDIR ${MG_PATH}

# UPDATING CONFIGURATION FILES
RUN chmod 777 webserverextensions/www/TempDir
RUN sed -i 's/AJP\/1\.3/HTTP\/1\.1/g' webserverextensions/tomcat/conf/server.xml

RUN rm -rf ${TEMPDIR}

# Log Files
RUN ln -sf /dev/stdout ${MGLOG_PATH}/{Access,Admin,Authentication}.log; \
    ln -sf /dev/stderr ${MGLOG_PATH}/Error.log; \
    ln -sf /dev/stdout ${MGAPACHE_LOG}/{access_,mod_jk.}log; \
    ln -sf /dev/stderr ${MGAPACHE_LOG}/error_log

COPY ./entrypoint.sh /
RUN chmod a+x /entrypoint.sh; \
    chmod a+rw ${MG_PATH}/webserverextensions/www/fusion/lib/tcpdf/cache/

EXPOSE 2810 2811 2812 8008 8009

ENTRYPOINT ["/entrypoint.sh"]
