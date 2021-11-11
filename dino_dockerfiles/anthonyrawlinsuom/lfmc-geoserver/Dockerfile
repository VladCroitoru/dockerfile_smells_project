#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
FROM tomcat:8.0-jre8
# PREVIOUS MAINTAINER Tim Sutton<tim@linfiniti.com>
MAINTAINER Anthony Rawlins<anthony.rawlins@unimelb.edu.au>

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl
#RUN  ln -s /bin/true /sbin/initctl

# Use local cached debs from host (saves your bandwidth!)
# Change ip below to that of your apt-cacher-ng host
# Or comment this line out if you do not with to use caching
ADD 71-apt-cacher-ng /etc/apt/apt.conf.d/71-apt-cacher-ng

# libc
#WORKDIR /

RUN apt-get -y update
# RUN apt-get -y upgrade
#RUN wget http://security-cdn.debian.org/pool/updates/main/l/linux/linux-libc-dev_4.9.82-1+deb9u3_amd64.deb
#RUN dpkg -i linux-libc-dev_4.9.82-1+deb9u3_amd64.deb
#RUN apt-get install -y build-essential apt-utils m4 curl libcurl4-openssl-dev


# zlib
#WORKDIR /
#RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/zlib-1.2.8.tar.gz
#RUN tar -zxvf zlib-1.2.8.tar.gz
#WORKDIR zlib-1.2.8
#RUN ./configure --prefix=/usr/local/libs/nc4libs
#RUN make install

# hdf5
#WORKDIR /
#RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/hdf5-1.8.13.tar.gz
#RUN tar -zxvf hdf5-1.8.13.tar.gz
#WORKDIR hdf5-1.8.13
#RUN ./configure --with-zlib=/usr/local/libs/nc4libs --prefix=/usr/local/libs/nc4libs --enable-threadsafe --with-pthread=/usr --enable-unsupported
#RUN make install

# netcdf
#WORKDIR /
#RUN wget https://github.com/Unidata/netcdf-c/archive/v4.6.0.tar.gz
#RUN tar -zxvf v4.6.0.tar.gz
#WORKDIR netcdf-c-4.6.0
#RUN CPPFLAGS=-I/usr/local/libs/nc4libs/include LDFLAGS=-L/usr/local/libs/nc4libs/lib ./configure --prefix=/usr/local/libs/nc4libs
#RUN make install

#-------------Application Specific Stuff ----------------------------------------------------

ENV GS_VERSION 2.14.2
ENV GEOSERVER_DATA_DIR /opt/geoserver/data_dir

RUN mkdir -p $GEOSERVER_DATA_DIR

# Unset Java related ENVs since they may change with Oracle JDK
ENV JAVA_VERSION=
ENV JAVA_DEBIAN_VERSION=

# Set JAVA_HOME to /usr/lib/jvm/default-java and link it to OpenJDK installation
RUN ln -s /usr/lib/jvm/java-8-openjdk-amd64 /usr/lib/jvm/default-java
ENV JAVA_HOME /usr/lib/jvm/default-java

ADD resources /tmp/resources

# If a matching Oracle JDK tar.gz exists in /tmp/resources, move it to /var/cache/oracle-jdk8-installer
# where oracle-java8-installer will detect it
RUN if ls /tmp/resources/*jdk-*-linux-x64.tar.gz > /dev/null 2>&1; then \
      mkdir /var/cache/oracle-jdk8-installer && \
      mv /tmp/resources/*jdk-*-linux-x64.tar.gz /var/cache/oracle-jdk8-installer/; \
    fi;

# Install Oracle JDK (and uninstall OpenJDK JRE) if the build-arg ORACLE_JDK = true or an Oracle tar.gz
# was found in /tmp/resources
ARG ORACLE_JDK=false
RUN if ls /var/cache/oracle-jdk8-installer/*jdk-*-linux-x64.tar.gz > /dev/null 2>&1 || [ "$ORACLE_JDK" = true ]; then \
       apt-get autoremove --purge -y openjdk-8-jre-headless && \
       echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true \
         | debconf-set-selections && \
       echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" \
         > /etc/apt/sources.list.d/webupd8team-java.list && \
       apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
       rm -rf /var/lib/apt/lists/* && \
       apt-get update && \
       apt-get install -y oracle-java8-installer oracle-java8-set-default && \
       ln -s --force /usr/lib/jvm/java-8-oracle /usr/lib/jvm/default-java && \
       rm -rf /var/lib/apt/lists/* && \
       rm -rf /var/cache/oracle-jdk8-installer; \
       if [ -f /tmp/resources/jce_policy.zip ]; then \
         unzip -j /tmp/resources/jce_policy.zip -d /tmp/jce_policy && \
         mv /tmp/jce_policy/*.jar $JAVA_HOME/jre/lib/security/; \
       fi; \
    fi;

WORKDIR /tmp

#Add JAI and ImageIO for great speedy speed.

# A little logic that will fetch the JAI and JAI ImageIO tar file if it
# is not available locally in the resources dir
RUN if [ ! -f /tmp/resources/jai-1_1_3-lib-linux-amd64.tar.gz ]; then \
    wget http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-amd64.tar.gz -P ./resources;\
    fi; \
    if [ ! -f /tmp/resources/jai_imageio-1_1-lib-linux-amd64.tar.gz ]; then \
    wget http://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz -P ./resources;\
    fi; \
    mv resources/jai-1_1_3-lib-linux-amd64.tar.gz ./ && \
    mv resources/jai_imageio-1_1-lib-linux-amd64.tar.gz ./ && \
    gunzip -c jai-1_1_3-lib-linux-amd64.tar.gz | tar xf - && \
    gunzip -c jai_imageio-1_1-lib-linux-amd64.tar.gz | tar xf - && \
    mv /tmp/jai-1_1_3/lib/*.jar $JAVA_HOME/jre/lib/ext/ && \
    mv /tmp/jai-1_1_3/lib/*.so $JAVA_HOME/jre/lib/amd64/ && \
    mv /tmp/jai_imageio-1_1/lib/*.jar $JAVA_HOME/jre/lib/ext/ && \
    mv /tmp/jai_imageio-1_1/lib/*.so $JAVA_HOME/jre/lib/amd64/ && \
    rm /tmp/jai-1_1_3-lib-linux-amd64.tar.gz && \
    rm -r /tmp/jai-1_1_3 && \
    rm /tmp/jai_imageio-1_1-lib-linux-amd64.tar.gz && \
    rm -r /tmp/jai_imageio-1_1
WORKDIR $CATALINA_HOME

RUN if [ ! -f /tmp/resources/geoserver-${GS_VERSION}-war.zip ]; then \
    wget -c http://downloads.sourceforge.net/project/geoserver/GeoServer/${GS_VERSION}/geoserver-${GS_VERSION}-war.zip \
      -O /tmp/resources/geoserver-${GS_VERSION}-war.zip; \
    fi; \
    unzip /tmp/resources/geoserver-${GS_VERSION}-war.zip -d /tmp/geoserver \
    && unzip /tmp/geoserver/geoserver.war -d $CATALINA_HOME/webapps/geoserver \
    && rm -rf $CATALINA_HOME/webapps/geoserver/data \
    && rm -rf /tmp/geoserver

# Install any plugin zip files in resources/plugins
RUN if ls /tmp/resources/plugins/*.zip > /dev/null 2>&1; then \
      for p in /tmp/resources/plugins/*.zip; do \
        unzip $p -d /tmp/gs_plugin \
        && mv /tmp/gs_plugin/*.jar $CATALINA_HOME/webapps/geoserver/WEB-INF/lib/ \
        && rm -rf /tmp/gs_plugin; \
      done; \
    fi

# Overlay files and directories in resources/overlays if they exist
RUN rm -f /tmp/resources/overlays/README.txt && \
    if ls /tmp/resources/overlays/* > /dev/null 2>&1; then \
      cp -rf /tmp/resources/overlays/* /; \
    fi;

ENV GEOSERVER_HOME $CATALINA_HOME/webapps/geoserver
# Create a GDAL_DATA environment variable to the folder where you have extracted this file.
# Make also sure that this directory is reachable and readable by the application server process’s user.
ENV GDAL_DATA /opt/gdal/gdal_data
RUN mkdir /gdaldata
RUN mkdir -p $GDAL_DATA

ENV GDAL_DIR /opt/gdal
RUN mkdir -p $GDAL_DIR
RUN mkdir ./gdal192

# Download Binary gdal192-Ubuntu12-gcc4.6.3-x86_64.tar.gz and move into place
# https://demo.geo-solutions.it/share/github/imageio-ext/releases/1.1.X/1.1.28/native/gdal/linux/gdal192-Ubuntu12-gcc4.6.3-x86_64.tar.gz
RUN if [ ! -f /tmp/resources/gdal192.tar.gz ]; then \
   wget https://demo.geo-solutions.it/share/github/imageio-ext/releases/1.1.X/1.1.28/native/gdal/linux/gdal192-Ubuntu12-gcc4.6.3-x86_64.tar.gz -O /tmp/resources/gdal192.tar.gz; \
   fi; \
   mv /tmp/resources/gdal192.tar.gz ./gdal192 && \
   gunzip -c ./gdal192/gdal192.tar.gz | tar xf - && \
   mv ./gdal192/* $GDAL_DIR && \
   rm -r ./gdal192

# The CRS definitions from gdal-data.zip
# Extract this archive on disk and place it in a proper directory on your system.
# https://demo.geo-solutions.it/share/github/imageio-ext/releases/1.1.X/1.1.28/native/gdal/gdal-data.zip
RUN if [ ! -f /tmp/resources/gdal-data.zip ]; then \
   wget https://demo.geo-solutions.it/share/github/imageio-ext/releases/1.1.X/1.1.28/native/gdal/gdal-data.zip -O /tmp/resources/gdal-data.zip; \
   fi; \
   mv /tmp/resources/gdal-data.zip /gdaldata && \
   unzip /gdaldata/gdal-data.zip && \
   mv /gdaldata/* $GDAL_DATA && \
   rm -r /gdaldata

ENV PATH "$PATH:/opt/gdal"

# Optionally remove Tomcat manager, docs, and examples
ARG TOMCAT_EXTRAS=true
RUN if [ "$TOMCAT_EXTRAS" = false ]; then \
    rm -rf $CATALINA_HOME/webapps/ROOT && \
    rm -rf $CATALINA_HOME/webapps/docs && \
    rm -rf $CATALINA_HOME/webapps/examples && \
    rm -rf $CATALINA_HOME/webapps/host-manager && \
    rm -rf $CATALINA_HOME/webapps/manager; \
  fi;

# Delete resources after installation
RUN rm -rf /tmp/resources

RUN apt-get install -y nano

ENV TZ Australia/Melbourne

EXPOSE 8080
