FROM apacheimages/oracle-jre-server:8u102b14
ENV NIFI_VERSION=1.0.0
ENV NIFI_HOME=/opt/local/nifi-${NIFI_VERSION}

WORKDIR /opt/local/src
RUN wget http://www-eu.apache.org/dist/nifi/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz && \
    tar zxf nifi-${NIFI_VERSION}-bin.tar.gz && \
    mv nifi-${NIFI_VERSION} ${NIFI_HOME} && \
    rm -rf *.tar.gz && \
    mkdir ${NIFI_HOME}/run ${NIFI_HOME}/logs && \
    apk del wget

WORKDIR /opt/local
RUN ln -s ${NIFI_HOME} /opt/local/nifi 

CMD ["/opt/local/nifi/bin/nifi.sh", "run"]
