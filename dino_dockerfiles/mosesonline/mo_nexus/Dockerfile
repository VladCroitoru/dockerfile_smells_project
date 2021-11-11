FROM sonatype/nexus:oss
MAINTAINER slawomir.messner@deutschebahn.com
ENV NEXUS_APT_PLUGIN_VERSION 1.1.2
ENV NEXUS_APT_PLUGIN_SHA 7dd1fa9899659d98f1143ac29cd4b900e98d4e34
USER root
RUN yum install -y unzip \
    && curl -fsSL https://github.com/inventage/nexus-apt-plugin/releases/download/nexus-apt-plugin-$NEXUS_APT_PLUGIN_VERSION/nexus-apt-plugin-$NEXUS_APT_PLUGIN_VERSION-bundle.zip -o /tmp/nexus-apt-plugin-$NEXUS_APT_PLUGIN_VERSION-bundle.zip \
    && echo "$NEXUS_APT_PLUGIN_SHA /tmp/nexus-apt-plugin-$NEXUS_APT_PLUGIN_VERSION-bundle.zip" | sha1sum -c \
    && unzip -d /opt/sonatype/nexus/nexus/WEB-INF/plugin-repository /tmp/nexus-apt-plugin-${NEXUS_APT_PLUGIN_VERSION}-bundle.zip \
    && find /opt/sonatype/nexus/nexus/WEB-INF/plugin-repository/nexus-apt-plugin-${NEXUS_APT_PLUGIN_VERSION} \
    -type d -exec chmod 755 {} \; \
    && find /opt/sonatype/nexus/nexus/WEB-INF/plugin-repository/nexus-apt-plugin-${NEXUS_APT_PLUGIN_VERSION} \
    -type f -exec chmod 644 {} \; \
    && yum remove -y unzip \
    && yum clean all && chown -R nexus:nexus ${SONATYPE_WORK}