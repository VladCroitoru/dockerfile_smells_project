FROM plone:4.3.19

ENV EDW_LOGGER_PUBLISHER=false \
    EDW_LOGGER_USER_ID=true \
    GRAYLOG=logcentral.eea.europa.eu:12201 \
    GRAYLOG_FACILITY=eea.docker.kgs \
    EEA_KGS_VERSION=21.11.4

LABEL eea-kgs-version=$EEA_KGS_VERSION \
      maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"

RUN mv /docker-entrypoint.sh /plone-entrypoint.sh \
 && mv -v versions.cfg plone-versions.cfg \
 && ls -a | grep .cfg | grep -v zope | grep -v plone | xargs rm

COPY src/docker/* /
COPY src/plone/* /plone/instance/
COPY packages/* /packages/
RUN /docker-setup.sh
