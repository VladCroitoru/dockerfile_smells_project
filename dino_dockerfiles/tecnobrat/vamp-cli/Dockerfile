FROM openjdk:8

ENV VAMP_CLI_VERSION=0.9.1
ENV WORKDIR=/opt/vamp

RUN mkdir -p ${WORKDIR} && \
  wget -nv -O /tmp/vamp-cli.zip https://bintray.com/artifact/download/magnetic-io/downloads/vamp-cli/vamp-cli-${VAMP_CLI_VERSION}.zip && \
  unzip -d ${WORKDIR} /tmp/vamp-cli.zip

WORKDIR "${WORKDIR}"

ENTRYPOINT ["java", "-jar", "vamp-cli.jar"]
