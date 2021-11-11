##############################################################################
# Dockerfile to build and run Jibiki lexical database server container images
# Based on openjdk
#############################################################################
#
# To debug, remove latest lines and launch the following commands:
# docker build -t jibikibuild .
# docker run --rm -it jibikibuild bash
#
#############################################################################
#
# Build part
#

FROM openjdk:8 as build
#FROM openjdk:15-slim-buster as build
#BUILD FAILED
#file:/jibiki/build.xml:333: org.enhydra.dods.generator.DODSGenerateException: java.lang.reflect.InvocationTargetException


LABEL maintainer="Mathieu.Mangeot@imag.fr"

ARG ADMIN_PASSWORD="dbpap"
ARG VALIDATOR_PASSWORD="butterfly"
ARG SPECIALIST_PASSWORD="farfalla"
ARG DATABASE_HOST="postgres"
ARG DATABASE_NAME="jibiki"
ARG DATABASE_USER="jibiki"
ARG DATABASE_PASSWORD="dbjibiki2"

ENV ADMIN_PASSWORD=$ADMIN_PASSWORD
ENV VALIDATOR_PASSWORD=$VALIDATOR_PASSWORD
ENV SPECIALIST_PASSWORD=$SPECIALIST_PASSWORD
ENV DATABASE_HOST=$DATABASE_HOST
ENV DATABASE_NAME=$DATABASE_NAME
ENV DATABASE_USER=$DATABASE_USER
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD

ENV LC_ALL C.UTF-8


#RUN apt-get update && apt-get install -y libpostgresql-jdbc-java
RUN apt-get update && apt-get install -y libpostgresql-jdbc-java git

WORKDIR /

RUN git clone "https://gricad-gitlab.univ-grenoble-alpes.fr/mmang/toolsforjibiki.git"

WORKDIR toolsforjibiki

RUN for file in *.tar.gz; do tar -zxf $file; done

WORKDIR enhydra5.1

#RUN ./configure -Djdk.dir=/usr/local/openjdk-8
 RUN ./configure -Djdk.dir=`which java | sed 's#/bin/java##'`

RUN chmod 755 bin/ant

RUN sed -i "s#CLASSPATH=#CLASSPATH=/toolsforjibiki/xalan-j_2_4_1/bin/xalan.jar:#" bin/ant

RUN cp ../xmlc-2.2.13/lib/xmlc.jar lib/.

RUN chmod -R 777 dods/build/template/standard/* && chmod 777 dods/build/dods.properties

WORKDIR /jibiki

COPY . .

RUN cp papillon.properties.in papillon.properties

RUN sed -i "s#\%TOOLSFORJIBIKI_DIR\%#/toolsforjibiki#g" papillon.properties \
   && sed -i "s#\%ADMIN_PASSWORD\%#$ADMIN_PASSWORD#g" papillon.properties \ 
   && sed -i "s#\%VALIDATOR_PASSWORD\%#$VALIDATOR_PASSWORD#g" papillon.properties \
   && sed -i "s#\%SPECIALIST_PASSWORD\%#$SPECIALIST_PASSWORD#g" papillon.properties \
   && sed -i "s#\%DATABASE_HOST\%#$DATABASE_HOST#g" papillon.properties \
   && sed -i "s#\%DATABASE_NAME\%#$DATABASE_NAME#g" papillon.properties \
   && sed -i "s#\%DATABASE_USER\%#$DATABASE_USER#g" papillon.properties \
   && sed -i "s#\%DATABASE_PASSWORD\%#$DATABASE_PASSWORD#g" papillon.properties

RUN /toolsforjibiki/enhydra5.1/bin/ant make

#############################################################################
#
# Run part
#
FROM openjdk:8-jre-alpine

ARG IPOLEX_DIR="/ipolex"
ENV IPOLEX_DIR=$IPOLEX_DIR

ENV LC_ALL C.UTF-8

WORKDIR $IPOLEX_DIR

WORKDIR /toolsforjibiki

COPY --from=build /toolsforjibiki/enhydra5.1/lib enhydra5.1/lib
COPY --from=build /toolsforjibiki/enhydra5.1/dods/lib enhydra5.1/dods/lib
COPY --from=build /toolsforjibiki/enhydra5.1/dods/build enhydra5.1/dods/build

COPY --from=build /toolsforjibiki/xalan-j_2_7_0 xalan-j_2_7_0
COPY --from=build /toolsforjibiki/fop-0.20.5 fop-0.20.5
COPY --from=build /toolsforjibiki/javamail-1.4 javamail-1.4

WORKDIR /jibiki

COPY --from=build /jibiki/papillon.properties .
COPY --from=build /jibiki/output output

#RUN echo `ls /usr/bin/java`

RUN java=`which java`; sed -i "s#JAVA=\"/usr/.*bin/java\"#JAVA=$java#" output/run
#RUN sed -i 's#JAVA="/usr/.*bin/java"#JAVA=/usr/bin/java#' output/run

WORKDIR /
COPY --from=build /usr/share/java/postgresql.jar /usr/share/java/postgresql.jar
COPY --from=build /jibiki/docker-entrypoint.sh .
COPY --from=build /jibiki/docker-entrypoint.d/* /docker-entrypoint.d/ 
ONBUILD COPY /jibiki/docker-entrypoint.d/* /docker-entrypoint.d/


##################### INSTALLATION END #####################

# Expose the default port
EXPOSE 8999

# Set default container command
#ENTRYPOINT /jibiki/output/run --debug --exec
#ENTRYPOINT /jibiki/docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh", "/jibiki/output/run"]
CMD ["--debug","--exec"]
