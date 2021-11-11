FROM maven:3.3-jdk-8
MAINTAINER Nathan Walker <nathan@rylath.net>

ENV TRANSITIMECORE /transitime-core
ENV PGPASSWORD=transitime
ENV AGENCYNAME=CAPMETRO
ENV AGENCYID=1
ENV GTFS_URL="https://data.texas.gov/download/r4v4-vz24/application/zip"
ENV GTFSRTVEHICLEPOSITIONS="https://data.texas.gov/download/eiei-9rpf/application/octet-stream"

RUN apt-get update \
	&& apt-get install -y postgresql-client \
	&& apt-get install -y git-core \
	&& apt-get install -y vim

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \
	05AB33110949707C93A279E3D3EFE6B686867BA6 \
	07E48665A34DCAFAE522E5E6266191C37C037D42 \
	47309207D818FFD8DCD3F83F1931D684307A10A5 \
	541FBE7D8F78B25E055DDEE13C370389288584E7 \
	61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \
	79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \
	9BA44C2621385CB966EBA586F72C284D731FABEE \
	A27677289986DB50844682F8ACB77FC2E86E29AC \
	A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \
	DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \
	F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \
	F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23

ENV TOMCAT_MAJOR 8
ENV TOMCAT_VERSION 8.0.36
ENV TOMCAT_TGZ_URL https://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz

RUN set -x \
	&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \
	&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \
	&& gpg --verify tomcat.tar.gz.asc \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
	&& rm bin/*.bat \
	&& rm tomcat.tar.gz*

EXPOSE 8080


# Install json parser so we can read API key for CreateAPIKey output

RUN wget http://stedolan.github.io/jq/download/linux64/jq

RUN chmod +x ./jq

RUN cp jq /usr/bin/

RUN git clone https://github.com/TheTransitClock/transitime.git /transitime-core

#RUN git clone https://github.com/Transitime/core.git /transitime-core

WORKDIR /transitime-core

#RUN git checkout kalman_predictions
RUN git checkout develop

#RUN git checkout shade_build_upstream

RUN mvn install -DskipTests

WORKDIR /
RUN mkdir /usr/local/transitime
RUN mkdir /usr/local/transitime/db
RUN mkdir /usr/local/transitime/config
RUN mkdir /usr/local/transitime/logs
RUN mkdir /usr/local/transitime/cache


# Deploy core. The work horse of transiTime.
RUN cp /transitime-core/transitime/target/*.jar /usr/local/transitime/

# Deploy API which talks to core using RMI calls.
RUN cp /transitime-core/transitimeApi/target/api.war  /usr/local/tomcat/webapps

# Deploy webapp which is a UI based on the API.
RUN cp /transitime-core/transitimeWebapp/target/web.war  /usr/local/tomcat/webapps

RUN cp /transitime-core/transitime/target/classes/ddl_postgres*.sql /usr/local/transitime/db

# RUN rm -rf /transitime-core
# RUN rm -rf ~/.m2/repository

# Scripts required to start transiTime. These are in the order they need to be run.
ADD bin/check_db_up.sh check_db_up.sh
ADD bin/generate_sql.sh generate_sql.sh
ADD bin/create_tables.sh create_tables.sh
ADD bin/create_api_key.sh create_api_key.sh
ADD bin/create_webagency.sh create_webagency.sh
ADD bin/import_gtfs.sh import_gtfs.sh
ADD bin/start_transitime.sh start_transitime.sh
ADD bin/get_api_key.sh	get_api_key.sh

# Handy utility to allow you connect directly to database
ADD bin/connect_to_db.sh connect_to_db.sh

# RUN ./generate_sql.sh

RUN \
	sed -i 's/\r//' *.sh &&\
 	chmod 777 *.sh

ADD config/postgres_hibernate.cfg.xml /usr/local/transitime/config/hibernate.cfg.xml
ADD config/transitime.properties /usr/local/transitime/config/transitime.properties
ADD config/transitime.properties /usr/local/transitimeTomcatConfig/transitime.properties
ADD config/transiTimeConfig.xml /usr/local/transitime/config/transiTimeConfig.xml

EXPOSE 8080

CMD ["/start_transitime.sh"]

