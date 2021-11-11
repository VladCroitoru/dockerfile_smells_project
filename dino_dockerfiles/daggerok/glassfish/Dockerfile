FROM openjdk:8u151-jdk-alpine
MAINTAINER Maksim Kostromin https://github.com/daggerok

ARG GLASSFISH_VERSION_ARG="5.0"
ARG GLASSFISH_ADMIN_PASSWORD_ARG="Admin.123"
ENV GLASSFISH_VERSION=${GLASSFISH_VERSION_ARG} \
    GLASSFISH_USER="glassfish5" \
    GLASSFISH_ADMIN_USER="admin" \
    GLASSFISH_ADMIN_PASSWORD=${GLASSFISH_ADMIN_PASSWORD_ARG}
ENV GLASSFISH_FILE="glassfish-${GLASSFISH_VERSION}.zip" \
    GLASSFISH_USER_HOME="/home/${GLASSFISH_USER}"
ENV GLASSFISH_HOME="${GLASSFISH_USER_HOME}/${GLASSFISH_USER}" \
    GLASSFISH_URL="http://download.oracle.com/glassfish/${GLASSFISH_VERSION}/release/${GLASSFISH_FILE}"

RUN apk --no-cache --update add busybox-suid bash wget ca-certificates unzip sudo openssh-client shadow \
 && addgroup ${GLASSFISH_USER}-group \
 && echo "${GLASSFISH_USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
 && sed -i "s/.*requiretty$/Defaults !requiretty/" /etc/sudoers \
 && adduser -h ${GLASSFISH_USER_HOME} -s /bin/bash -D -u 1025 ${GLASSFISH_USER} ${GLASSFISH_USER}-group \
 && usermod -a -G wheel ${GLASSFISH_USER} \
 && wget --no-cookies \
         --no-check-certificate \
         --header "Cookie: oraclelicense=accept-securebackup-cookie" \
                  "http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip" \
         -O /tmp/jce_policy-8.zip \
 && unzip -o /tmp/jce_policy-8.zip -d /tmp \
 && mv -f ${JAVA_HOME}/lib/security ${JAVA_HOME}/lib/backup-security || true \
 && mv -f /tmp/UnlimitedJCEPolicyJDK8 ${JAVA_HOME}/lib/security \
 && apk --no-cache --no-network --purge del busybox-suid ca-certificates unzip shadow \
 && rm -rf /var/cache/apk/* /tmp/*

USER ${GLASSFISH_USER}
WORKDIR ${GLASSFISH_USER_HOME}

CMD /bin/bash
EXPOSE 8080 4848
ENTRYPOINT /bin/bash ${GLASSFISH_HOME}/bin/asadmin start-domain domain1 \
        && tail -f ${GLASSFISH_HOME}/glassfish/domains/domain1/logs/server.log

RUN wget ${GLASSFISH_URL} -O ${GLASSFISH_USER_HOME}/${GLASSFISH_FILE} \
 && unzip ${GLASSFISH_USER_HOME}/${GLASSFISH_FILE} -d ${GLASSFISH_USER_HOME} \
 && rm -rf ${GLASSFISH_USER_HOME}/${GLASSFISH_FILE} \
 && echo "AS_ADMIN_PASSWORD=" >> ${GLASSFISH_HOME}/bin/tempfile \
 && echo "AS_ADMIN_NEWPASSWORD=${GLASSFISH_ADMIN_PASSWORD}" >> ${GLASSFISH_HOME}/bin/tempfile \
 && echo "AS_ADMIN_PASSWORD=${GLASSFISH_ADMIN_PASSWORD}" >> ${GLASSFISH_HOME}/bin/passwordfile \
 && /bin/bash ${GLASSFISH_HOME}/bin/asadmin restart-domain domain1 \
 && /bin/bash ${GLASSFISH_HOME}/bin/asadmin --user=${GLASSFISH_ADMIN_USER} --passwordfile=${GLASSFISH_HOME}/bin/tempfile change-admin-password \
 && /bin/bash ${GLASSFISH_HOME}/bin/asadmin --host 0.0.0.0 --port 4848 --user=${GLASSFISH_ADMIN_USER} --passwordfile=${GLASSFISH_HOME}/bin/passwordfile enable-secure-admin \
 && /bin/bash ${GLASSFISH_HOME}/bin/asadmin restart-domain domain1 \
 && /bin/bash ${GLASSFISH_HOME}/bin/asadmin stop-domain domain1

#################################################### USAGE ######################################################
# FROM daggerok/glassfish                                                                                       #
# HEALTHCHECK --timeout=2s --retries=22 \                                                                       #
#         CMD wget -q --spider http://127.0.0.1:8080/my-service/health \                                        #
#          || exit 1                                                                                            #
# COPY --chown=glassfish5 ./target/*.war ${GLASSFISH_HOME}/glassfish/domains/domain1/autodeploy/my-service.war  #
#################################################################################################################

###################################### DEBUG | MULTI-DEPLOYMENTS USAGE ##########################################
# FROM daggerok/glassfish:5.0-web-alpine                                                                        #
# # Debug:                                                                                                      #
# ENV JAVA_OPTS="$JAVA_OPTS -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005"                 #
# EXPOSE 5005                                                                                                   #
# # Multi builds:                                                                                               #
# COPY --chown=glassfish5 ./app.ear ./path/to/*.war ${GLASSFISH_HOME}/glassfish/domains/domain1/autodeploy/     #
#################################################################################################################
