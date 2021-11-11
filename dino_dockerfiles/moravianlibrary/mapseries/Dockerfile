FROM jboss/wildfly:16.0.0.Final

COPY scripts /scripts
COPY configs /configs

USER root
RUN /scripts/setup.sh
RUN rm -rf /scripts /configs

ENV LANG en_US.utf8

COPY catalog /build/catalog
COPY edit /build/edit
COPY index /build/index

RUN chown -R jboss:jboss /build
USER jboss

RUN /build/catalog/docker.sh && \
    /build/edit/docker.sh && \
    /build/index/docker.sh && \
    rm -rf /build/*

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-c", "standalone-full-mapseries.xml"]
