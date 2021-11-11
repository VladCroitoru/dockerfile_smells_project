##### USAGE BEGIN #####
#
# # apply base image:
# FROM daggerok/apache-tomcat:9.0.37
#
# # healthy check:
# HEALTHCHECK --start-period=1s --interval=1s --timeout=5s --retries=33 \
#         CMD wget -q --spider http://127.0.0.1:8080/health/ || exit 1
#
# # debug:
# ARG JPDA_OPTS_ARG="${JAVA_OPTS} -agentlib:jdwp=transport=dt_socket,address=1043,server=y,suspend=n"
# ENV JPDA_OPTS="${JPDA_OPTS_ARG}"
# EXPOSE 5005
#
# # deploy apps:
# COPY --chwon=tomcat ./path/to/*.war ./path/to/another/*.war ${TOMCAT_HOME}/webapps/
#
##### USAGE END #####

FROM openjdk:8u212-jdk-alpine3.9
LABEL MAINTAINER="Maksim Kostromin https://github.com/daggerok/docker"

ARG TOMCAT_RELEASE=9
ARG TOMCAT_VERSION=9.0.37
ARG TOMCAT_USER_ARG="tomcat"
ARG TOMCAT_FILE_ARG="apache-tomcat-${TOMCAT_VERSION}"
ARG TOMCAT_URL_ARG="https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_RELEASE}/v${TOMCAT_VERSION}/bin/${TOMCAT_FILE_ARG}.zip"

ENV JAVA_VERSION="8"
ENV TOMCAT_USER=${TOMCAT_USER_ARG}                                                                                                \
    TOMCAT_GROUP=${TOMCAT_USER_ARG}-group                                                                                         \
    TOMCAT_FILE=${TOMCAT_FILE_ARG}                                                                                                \
    TOMCAT_URL=${TOMCAT_URL_ARG}
ENV TOMCAT_USER_HOME="/home/${TOMCAT_USER}"
ENV TOMCAT_HOME="${TOMCAT_USER_HOME}/${TOMCAT_FILE}"

EXPOSE 8080
ENTRYPOINT ["/bin/ash", "-c"]
CMD ["                                    \
  ash ${TOMCAT_HOME}/bin/catalina.sh run  \
"]

RUN apk --no-cache --update add busybox-suid wget ca-certificates unzip sudo openssh-client shadow                                \
 && addgroup ${TOMCAT_GROUP}                                                                                                      \
 && echo "${TOMCAT_USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers                                                                 \
 && sed -i "s/.*requiretty$/Defaults !requiretty/" /etc/sudoers                                                                   \
 && adduser -h ${TOMCAT_USER_HOME} -s /bin/ash -D -u 1025 ${TOMCAT_USER} ${TOMCAT_GROUP}                                          \
 && usermod -a -G wheel ${TOMCAT_USER}                                                                                            \
 && apk --no-cache --no-network --purge del busybox-suid ca-certificates unzip shadow                                             \
 && rm -rf /var/cache/apk/* /tmp/*

USER ${TOMCAT_USER}
WORKDIR ${TOMCAT_USER_HOME}

RUN wget -q  ${TOMCAT_URL} -O "${TOMCAT_USER_HOME}/${TOMCAT_FILE}.zip"                                                            \
 && unzip -q ${TOMCAT_USER_HOME}/${TOMCAT_FILE}.zip -d ${TOMCAT_USER_HOME}                                                        \
 && rm -rf   ${TOMCAT_USER_HOME}/${TOMCAT_FILE}.zip                                                                               \
 && mkdir -p ${TOMCAT_HOME}/logs && touch ${TOMCAT_HOME}/logs/catalina.out                                                        \
 && chown -R ${TOMCAT_USER}:${TOMCAT_USER} ${TOMCAT_HOME}/logs
