FROM schemaspy/schemaspy:snapshot
ENV H2_VERSION=1.4.196
LABEL H2_VERSION=1.4.196

USER root
RUN apk add --no-cache curl && \
    cd /drivers_inc && \
    curl -JLO http://search.maven.org/remotecontent?filepath=com/h2database/h2/$H2_VERSION/h2-$H2_VERSION.jar && \
    chown -R java /drivers_inc/h2-$H2_VERSION.jar && \
    apk del curl
USER java
