FROM eeacms/reportek-base-dr:2.5.3
MAINTAINER "Olimpiu Rob" <olimpiu.rob@eaudeweb.ro>

ENV DATADICTIONARY_SCHEMAS_URL=http://dd.eionet.europa.eu/api/schemas/forObligation \
    UNS_NOTIFICATIONS=on \
    REDIS_DATABASE=1 \
    REDIS_HOSTNAME=redisdeploy \
    SESSION_MANAGER_TIMEOUT=120 \
    REPORTEK_DEPLOYMENT=CDR

COPY src/sources.cfg                \
     src/cdr-instance.cfg           \
     src/tests.cfg                  \
     src/base.cfg                   $ZOPE_HOME/
COPY src/docker-initialize.py       /

USER root
RUN ./install.sh
USER zope-www
