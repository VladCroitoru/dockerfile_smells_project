FROM polyglotted/java-base
MAINTAINER pgtdev@polyglotted.io

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

ENV DS_VER M24
ENV DS_NAME apacheds-2.0.0-${DS_VER}
WORKDIR /tmp

RUN apk add --update zip unzip openldap-clients wget && \
	mkdir -p /opt && \
	cd /opt && \
	wget --no-check-certificate https://www.apache.org/dist/directory/apacheds/dist/2.0.0-${DS_VER}/${DS_NAME}.zip && \
	unzip ${DS_NAME}.zip && \
	apk del zip unzip && \
	rm ${DS_NAME}.zip

WORKDIR /opt/${DS_NAME}

COPY files/config.ldif /opt/${DS_NAME}/instances/default/conf/
COPY files/adminpwd.ldif /tmp/
COPY files/sample.ldif /tmp/
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Polyglotted ApacheDS" \
      org.label-schema.description="Apache Directory Server container" \
      org.label-schema.url="http://polyglotted.io" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/polyglotted/apacheds" \
      org.label-schema.vendor="Polyglotted Limited" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

RUN chmod ugo+x bin/apacheds.sh && \
    bin/apacheds.sh start && sleep 10 && \
    ldapmodify -h 127.0.0.1 -p 10389 -x -a -f /tmp/sample.ldif &&  \
    ldapmodify -h 127.0.0.1 -p 10389 -x -D "uid=admin,ou=system" -w secret -f /tmp/adminpwd.ldif &&  \
    bin/apacheds.sh stop && sleep 5 && \
    rm /tmp/adminpwd.ldif && \
    rm /tmp/sample.ldif

EXPOSE 10389
CMD ["bin/apacheds.sh", "default", "run"]
