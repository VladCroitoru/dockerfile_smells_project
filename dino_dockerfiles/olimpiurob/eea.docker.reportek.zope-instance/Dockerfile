FROM eeacms/zope:latest
MAINTAINER "Olimpiu Rob" <olimpiu.rob@eaudeweb.ro>

COPY src/versions.cfg $ZOPE_HOME/
COPY src/sources.cfg $ZOPE_HOME/
COPY src/base.cfg $ZOPE_HOME/

RUN ./install.sh
