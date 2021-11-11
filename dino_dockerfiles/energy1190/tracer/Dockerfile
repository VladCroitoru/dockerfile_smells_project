FROM buildpack-deps:jessie-curl

ENV TS_VER 4020


ENV TS_LOG_LEVEL INFO

ENV TS_ADMIN=admin
ENV TS_URL 'http\://localhost\:8080'
ENV TS_UPLOAD /ts/upload
ENV TS_INDEX /ts/index

ENV TS_DB_USER postgres
ENV TS_DB_PASS postgres
ENV TS_DB_URL 'jdbc\:postgresql\://127.0.0.1\:5432/trackstudio'

ENV TS_LIC_TYPE EVAL
ENV TS_LIC_NAME 'Evaluation Customer'
#ENV TS_LIC_DATE
#ENV TS_LIC_SUPPORT
#ENV TS_LIC_IP
ENV TS_LIC_KEY TSL105580-7e767f1c7d148ea98bc7a836bc7e6e96

ENV TS_MAIL_FROM trackstudio
ENV TS_MAIL_SMTP_HOST 127.0.0.1
ENV TS_MAIL_SMTP_PORT 25
ENV TS_MAIL_NOTIFY no

ENV TS_SCM_SVN_INIT_REV 1
ENV TS_SCM_SVN_USER svn
ENV TS_SCM_SVN_PASS svn
ENV TS_SCM_SVN_ROOT 'svn://server/svn/repo'
ENV TS_SCM_SVN_TYPE Subversion
ENV TS_SCM_SVN_ENABLE no

ENV TS_LDAP_ENABLE no
ENV TS_LDAP_HOST 127.0.0.1
ENV TS_LDAP_PORT 389
ENV TS_LDAP_SSL no
ENV TS_LDAP_USER ldap
ENV TS_LDAP_PASS ldap
ENV TS_LDAP_FILTER (&(objectClass=*)(sAMAccountName={0}))

ENV TS_CONFIG /ts/etc

ENV CONFD_VERSION 0.11.0

# install confd
RUN curl -sSL https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 -o /usr/local/bin/confd && \
chmod +x /usr/local/bin/confd

RUN mkdir -p /app
ADD confd.toml /app/confd.toml
ADD templates /app/templates
ADD conf.d /app/conf.d

# http://download.trackstudio.com/tse-40/TrackStudio_4019_unix_x64.tar.gz

RUN wget http://download.trackstudio.com/tse-40/TrackStudio_${TS_VER}_unix_x64.tar.gz && \
tar -xf TrackStudio_${TS_VER}_unix_x64.tar.gz && \
mv TrackStudio-${TS_VER} ts && \
sed -i "s/8888/8080/g" /ts/jetty/etc/jetty.xml && \
rm -f TrackStudio_${TS_VER}_unix_x64.tar.gz

RUN mkdir -p ${TS_UPLOAD}

VOLUME ${TS_UPLOAD}
VOLUME ${TS_INDEX}

ADD entrypoint.sh /
RUN chmod 500 /entrypoint.sh

ADD check_https /
RUN chmod 500 /check_https

EXPOSE 8080
EXPOSE 8443
ENTRYPOINT ["/entrypoint.sh"]
CMD [""]