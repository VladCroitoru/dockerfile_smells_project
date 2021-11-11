FROM sergef/docker-library-alpine:edge

ENV LICENSE use-your-own==
ENV JETTY_PORT 80
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH ${PATH}:${JAVA_HOME}/bin
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:/usr/bin

EXPOSE $JETTY_PORT

COPY ./entrypoint.sh /app/

# Login to https://structurizr.com/dashboard and download
# https://structurizr.com/user/download/structurizr-onpremises-ui.war
COPY ./structurizr-onpremises-ui.war /app/

RUN apk add --no-cache \
    openjdk8-jre@community \
    jetty-runner@community \
    openssl \
    tini@community \
    unzip \
  && rm -rf \
    /tmp/* \
    /var/cache/apk/* \
  && chmod +x /app/entrypoint.sh \
  && mkdir -p /appdata/structurizr /app/structurizr-onpremises-ui \
  && unzip /app/structurizr-onpremises-ui.war -d /app/structurizr-onpremises-ui

COPY ./jetty-env.xml /app/structurizr-onpremises-ui/WEB-INF/

ENTRYPOINT ["/sbin/tini", "-s", "-g", "--", "/app/entrypoint.sh"]
