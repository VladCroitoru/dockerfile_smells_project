FROM java:openjdk-8-jdk

RUN groupadd -r confluence && useradd -r -g confluence confluence
ENV CONF_HOME /opt/confluence
ENV CONF_DATA /data/confluence

RUN apt-get update -q && apt-get install -y wget curl mysql-client \
  && apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin
  
RUN mkdir -p "${CONF_HOME}" && mkdir -p "${CONF_DATA}"\
  && curl -Ls https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-6.0.2.tar.gz | \
  tar -xz --directory "${CONF_HOME}" --strip-components=1
  
RUN mkdir -p ${CONF_DATA}/temp && mkdir ${CONF_DATA}/logs && mkdir ${CONF_DATA}/work \
  && chown -R confluence:confluence "${CONF_DATA}" \
  && echo -e "\nconfluence.home=${CONF_DATA}" >> "${CONF_HOME}/confluence/WEB-INF/classes/confluence-init.properties"
  
WORKDIR ${CONF_HOME}
EXPOSE 8090
EXPOSE 8080
CMD ["sh","./bin/catalina.sh","run"]
