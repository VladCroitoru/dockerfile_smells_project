FROM ubuntu:20.04

ENV LANG='en_US.UTF-8' \
    LANGUAGE='en_US:en' \
    LC_ALL='en_US.UTF-8'

ARG SONARQUBE_VERSION=9.1.0.47736
ARG SONARQUBE_ZIP_URL=https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-${SONARQUBE_VERSION}.zip
ARG SONAR_SCANNER_VERSION=4.6.2.2472
ARG SONAR_SCANNER_URL=https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

RUN apt-get -y update

RUN apt-get install -y openjdk-11-jdk

RUN apt-get install -y nodejs

RUN apt-get install -y python3 python3-pip

RUN apt-get install -y \
    nmap ncat \
    wget curl \
    zip \
    net-tools \
    python3 \
    jq \
    shellcheck

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 \
    SONARQUBE_HOME=/opt/sonarqube \
    SONAR_SCANNER_HOME=/opt/sonar-scanner \
    DEBIAN_FRONTEND=noninteractive \
    HOME=/tmp \
    XDG_CONFIG_HOME=/tmp \
    NODE_PATH=/usr/lib/node_modules \
    SRC_PATH=/opt/src

ENV PATH="/opt/sonar-sa/entrypoint:/opt/java/openjdk/bin:$PATH"

WORKDIR /opt

RUN set -eux && \
    wget --progress=dot -e dotbytes=1M -O sonarqube.zip "${SONARQUBE_ZIP_URL}" && \
    unzip -q sonarqube.zip && \
    mv "sonarqube-${SONARQUBE_VERSION}" sonarqube && \
    rm sonarqube.zip

RUN set -eux && \
    wget --progress=dot -e dotbytes=64K -O sonar-scanner-cli.zip "${SONAR_SCANNER_URL}" && \
    unzip -q sonar-scanner-cli.zip && \
    mv "sonar-scanner-${SONAR_SCANNER_VERSION}" sonar-scanner && \
    rm sonar-scanner-cli.zip

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir pylint

RUN useradd -m sonarqube

COPY --chown=sonarqube:sonarqube entrypoint /opt/sonar-sa/entrypoint

RUN set -eux && \
    mkdir "/opt/sonar-sa/src" "/opt/sonar-sa/logs" "${SONAR_SCANNER_HOME}/.sonar" && \
    chown -R sonarqube:sonarqube sonarqube && \
    chown -R sonarqube:sonarqube "${SONAR_SCANNER_HOME}" "/opt/sonar-sa" && \
    chmod +x \
        sonar-sa/entrypoint/sonar-sa.sh \
        sonar-sa/entrypoint/entrypoint.sh && \ 
    chmod -R 777 sonarqube/data sonarqube/extensions sonarqube/logs sonarqube/temp && \
    chmod -R 777 "/opt/sonar-sa/src" "${SONAR_SCANNER_HOME}/.sonar"

WORKDIR /opt/sonar-sa
USER sonarqube

ENTRYPOINT ["/opt/sonar-sa/entrypoint/entrypoint.sh"]
CMD [ "entrypoint/sonar-sa.sh", "main" ]

# CMD ["/opt/sonarqube/bin/sonar-sa.sh"]

#     apk add --no-cache --virtual build-dependencies gnupg unzip curl; \
#     apk add --no-cache bash su-exec ttf-dejavu openjdk11-jre; \
#     # pub   2048R/D26468DE 2015-05-25
#     #       Key fingerprint = F118 2E81 C792 9289 21DB  CAB4 CFCA 4A29 D264 68DE
#     # uid                  sonarsource_deployer (Sonarsource Deployer) <infra@sonarsource.com>
#     # sub   2048R/06855C1D 2015-05-25
#     echo "networkaddress.cache.ttl=5" >> "${JAVA_HOME}/conf/security/java.security"; \
#     sed --in-place --expression="s?securerandom.source=file:/dev/random?securerandom.source=file:/dev/urandom?g" "${JAVA_HOME}/conf/security/java.security"; \
#     for server in $(shuf -e ha.pool.sks-keyservers.net \
#                             hkp://p80.pool.sks-keyservers.net:80 \
#                             keyserver.ubuntu.com \
#                             hkp://keyserver.ubuntu.com:80 \
#                             pgp.mit.edu) ; do \
#         gpg --batch --keyserver "${server}" --recv-keys 679F1EE92B19609DE816FDE81DB198F93525EC1A && break || : ; \
#     done; \
#     mkdir --parents /opt; \
#     cd /opt; \
#     curl --fail --location --output sonarqube.zip --silent --show-error "${SONARQUBE_ZIP_URL}"; \
#     curl --fail --location --output sonarqube.zip.asc --silent --show-error "${SONARQUBE_ZIP_URL}.asc"; \
#     gpg --batch --verify sonarqube.zip.asc sonarqube.zip; \
#     unzip -q sonarqube.zip; \
#     mv "sonarqube-${SONARQUBE_VERSION}" sonarqube; \
#     rm sonarqube.zip*; \
#     rm -rf ${SONARQUBE_HOME}/bin/*; \
#     chown -R sonarqube:sonarqube ${SONARQUBE_HOME}; \
#     # this 777 will be replaced by 700 at runtime (allows semi-arbitrary "--user" values)
#     chmod -R 777 "${SQ_DATA_DIR}" "${SQ_EXTENSIONS_DIR}" "${SQ_LOGS_DIR}" "${SQ_TEMP_DIR}"; \
#     apk del --purge build-dependencies;

# COPY --chown=sonarqube:sonarqube run.sh sonar.sh ${SONARQUBE_HOME}/bin/

# WORKDIR ${SONARQUBE_HOME}
# EXPOSE 9000

# STOPSIGNAL SIGINT

# ENTRYPOINT ["/opt/sonarqube/bin/run.sh"]
# CMD ["/opt/sonarqube/bin/sonar.sh"]