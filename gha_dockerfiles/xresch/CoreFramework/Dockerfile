FROM --platform=linux/amd64 openjdk:8

ENV BASEDIR=/usr/src/cfw-server/
ENV DATAMOUNT=/data

VOLUME ${DATAMOUNT}

WORKDIR ${BASEDIR} 
COPY ./config ${BASEDIR}/config/
COPY ./resources/ ${BASEDIR}/resources/
COPY ./scripts/docker_start.sh ./start.sh
COPY ./scripts/docker_stop.sh ./stop.sh

COPY ./target/lib ${BASEDIR}/lib/
COPY ./target/cfw-?.?.?.jar ${BASEDIR}/lib/

#HTTP
EXPOSE 8888
#JDBC Database
EXPOSE 8889

# Change Config File path to /data/mount
RUN sed -i 's/.\/config/\/data\/config/g' ${BASEDIR}/config/cfw.properties

# Change Datastore File path
RUN sed -i 's/cfw_h2_path=.\/datastore/cfw_h2_path=\/data\/datastore/g' ${BASEDIR}/config/cfw.properties

# Change Log File path
RUN sed -i 's/.\/log\//\/data\/log\//g' ${BASEDIR}/config/logging.properties

CMD ./start.sh

