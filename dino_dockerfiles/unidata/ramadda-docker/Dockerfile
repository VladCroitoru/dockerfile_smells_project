###
# Dockerfile for RAMADDA
###

FROM unidata/tomcat-docker:8.5

###
# Usual maintenance
###

USER root

RUN apt-get update

###
# Create data directory
###

ENV DATA_DIR /data/repository

RUN mkdir -p ${DATA_DIR}

###
# Grab RAMADDA
###

RUN curl -SL \
  https://geodesystems.com/repository/entry/get/repository.war?entryid=synth%3A498644e1-20e4-426a-838b-65cffe8bd66f%3AL3JlcG9zaXRvcnkud2Fy \
  -o ${CATALINA_HOME}/webapps/repository.war

###
# Tomcat Java and Catalina Options
###

COPY files/setenv.sh ${CATALINA_HOME}/bin/setenv.sh

COPY files/javaopts.sh ${CATALINA_HOME}/bin/javaopts.sh

COPY startram.sh ${CATALINA_HOME}/bin/

RUN chmod +x ${CATALINA_HOME}/bin/*.sh

WORKDIR ${DATA_DIR}

###
# Entrypoint
###

COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

###
# Start container
###

CMD ["startram.sh"]
