FROM openjdk:8-jre
LABEL maintainer="Mohammed alsahli <mohmmad1024@gmail.com>"

ARG SAM_VERSION=0.6.0
ARG DOWNLOAD_URL=https://github.com/hortonworks/streamline/releases/download/v0.6.0/hortonworks-streamline-0.6.0.tar.gz

ENV BASE_DIR /sam 

RUN mkdir -p ${BASE_DIR} && cd ${BASE_DIR}\
    && curl -fSL ${DOWNLOAD_URL} -o sam.tar.gz \
    && tar -xvzf ${BASE_DIR}/sam.tar.gz -C ${BASE_DIR} --strip-components=1 \
    && rm -f sam.tar.gz

EXPOSE 8080 8081

WORKDIR ${BASE_DIR}
ADD mysql-connector-java-5.1.46.jar ${BASE_DIR}/libs/
ADD mysql-connector-java-5.1.46.jar ${BASE_DIR}/bootstrap/lib/
ADD yq_linux_386 /usr/bin/yq
ADD scripts/ ${BASE_DIR}/scripts/
RUN chmod +x /usr/bin/yq && chmod -R +x ${BASE_DIR}/scripts/

CMD ${BASE_DIR}/scripts/moh_docker_start.sh
