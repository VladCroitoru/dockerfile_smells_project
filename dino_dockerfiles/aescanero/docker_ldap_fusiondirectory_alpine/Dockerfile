FROM alpine:edge
MAINTAINER Alejandro Escanero Blanco <aescanero@gmail.com>

LABEL maintainer="Alejandro Escanero Blanco <aescanero@gmail.com>" \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.name="Openldap for FusionInventory on Alpine OS" \
      org.label-schema.url="https://www.disasterproject.com" \
      org.label-schema.vcs-url="https://github.com/aescanero/dockerevents/docker-openldap-alpine.git"


ENV SUPERVISOR_VERSION=3.3.0
RUN apk update && apk add -u python py2-pip py-pyldap openldap openldap-back-monitor bash wget perl\
  && pip install supervisor==$SUPERVISOR_VERSION && pip install python-rest-client python-daemon 
ADD etc/supervisord-be.conf /etc/supervisord.conf
ADD apps/watcher/watcher.py /usr/local/sbin/watcher.py
ADD ldap/slapd.conf /etc/openldap/slapd.conf
ADD ldap/fd.ldif /etc/openldap/fd.ldif

RUN mkdir -p /svr/config && adduser -S openldap \
  && mkdir -p /data/schema && cd /data/schema \
  && mkdir -p /data/pids && mkdir -p /data/logs && mkdir /data/ldap && mkdir /etc/openldap/slapd.d \
  && wget --no-check-certificate https://github.com/fusiondirectory/schema2ldif/archive/master.zip \
  && unzip master.zip \
  && wget --no-check-certificate https://raw.githubusercontent.com/fusiondirectory/fusiondirectory/master/contrib/openldap/core-fd-conf.schema \
  https://raw.githubusercontent.com/fusiondirectory/fusiondirectory/master/contrib/openldap/core-fd.schema \
  https://raw.githubusercontent.com/fusiondirectory/fusiondirectory/master/contrib/openldap/ldapns.schema \
  https://raw.githubusercontent.com/fusiondirectory/fusiondirectory/master/contrib/openldap/rfc2307bis.schema \
  https://raw.githubusercontent.com/fusiondirectory/fusiondirectory/master/contrib/openldap/template-fd.schema \
  && perl schema2ldif-master/bin/schema2ldif core-fd-conf.schema >core-fd-conf.ldif \
  && perl schema2ldif-master/bin/schema2ldif core-fd.schema >core-fd.ldif \
  && perl schema2ldif-master/bin/schema2ldif ldapns.schema >ldapns.ldif \
  && perl schema2ldif-master/bin/schema2ldif rfc2307bis.schema >rfc2307bis.ldif \
  && perl schema2ldif-master/bin/schema2ldif template-fd.schema >template-fd.ldif \
  && ! /usr/sbin/slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d -Q 2>/dev/null \
  && /usr/sbin/slapadd -F /etc/openldap/slapd.d -n 0 -l core-fd.ldif \
  && /usr/sbin/slapadd -F /etc/openldap/slapd.d -n 0 -l core-fd-conf.ldif \
  && echo "ns" && /usr/sbin/slapadd -F /etc/openldap/slapd.d -n 0 -l ldapns.ldif \
  && /usr/sbin/slapadd -F /etc/openldap/slapd.d -n 0 -l template-fd.ldif \
  && /usr/sbin/slapadd -F /etc/openldap/slapd.d -n 1 -l /etc/openldap/fd.ldif \
  && chown openldap /etc/openldap/slapd.d -R \
  && chown openldap /data/ldap -R \
  && chown openldap /var/run/openldap \
  && chmod u+x /usr/local/sbin/watcher.py \
  && rm -rf /var/cache/apk/*


WORKDIR /data
#CMD ["sh"]
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
