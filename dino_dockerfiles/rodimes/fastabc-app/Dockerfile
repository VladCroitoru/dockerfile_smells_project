FROM rodimes/spring-boot

MAINTAINER Rodrigo <rodimes@gmail.com>

ARG FASTABC_FOLDER=/opt/fastabc-app/
ARG PATH_JAR=s3-sa-east-1.amazonaws.com/fastabc/app/fastabc.jar
ENV JAVA_TIMEZONE=America/Sao_Paulo
ENV JAVA_OPTS="-XX:-OmitStackTraceInFastThrow -Xmx512m"

RUN touch /tmp/test.mv.db
COPY ./bin/after.sh /opt/app

USER root
RUN mkdir -p ${FASTABC_FOLDER}

RUN cd ${FASTABC_FOLDER} && curl -O https://${PATH_JAR} &&  chmod 777 fastabc.jar

EXPOSE 8081
CMD ["/opt/app/after.sh"]
