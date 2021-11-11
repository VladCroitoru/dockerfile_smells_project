# Lastest visono/debian_serf_jre
FROM visono/debian_serf_jre:latest

MAINTAINER Patrik Hagedorn <p.hagedorn@visono.com>

USER root

# Install Jetty 9
WORKDIR /opt

ENV JETTY_VERSION="9.3.14.v20161028"

# Downloading latest jetty distribution
RUN wget -O jetty.tar.gz "http://central.maven.org/maven2/org/eclipse/jetty/jetty-distribution/${JETTY_VERSION}/jetty-distribution-${JETTY_VERSION}.tar.gz" \
    && mkdir jetty \
    && tar -xvf jetty.tar.gz -C jetty --strip-components 1 \
    && rm /opt/jetty.tar.gz \
    && useradd jetty -U -s /bin/false \
    && chown -R jetty:jetty /opt/jetty

# Adding Jetty configuration
COPY start.ini /opt/jetty/start.ini
COPY http.ini /opt/jetty/start.d/http.ini

CMD ["/bin/bash"]