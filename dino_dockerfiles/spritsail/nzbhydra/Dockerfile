FROM spritsail/alpine:3.14

ARG NZBHYDRA_VER=3.17.3
ARG NZBHYDRA_URL="https://github.com/theotherp/nzbhydra2/releases/download/v${NZBHYDRA_VER}/nzbhydra2-${NZBHYDRA_VER}-linux.zip"

ARG YQ_VER=v4.14.1
ARG YQ_ARCH=amd64

ENV SUID=907 SGID=900
ENV MAXMEM=256M
ENV NZBHYDRA_DIR=/usr/lib/nzbhydra

LABEL maintainer="Spritsail <nzbhydra@spritsail.io>" \
      org.label-schema.vendor="Spritsail" \
      org.label-schema.name="NZBHydra 2" \
      org.label-schema.url="https://github.com/theotherp/nzbhydra2" \
      org.label-schema.description="NZBHydra is a meta search for NZB indexers" \
      org.label-schema.version=${NZBHYDRA_VER} \
      io.spritsail.version.nzbhydra=${NZBHYDRA_VER}

WORKDIR $NZBHYDRA_DIR

RUN apk add --no-cache openjdk11-jre nss \
 && wget -O /tmp/nzbhydra2.zip $NZBHYDRA_URL \
 && unzip -d /tmp /tmp/nzbhydra2.zip \
 && cp /tmp/lib/core-${NZBHYDRA_VER}-exec.jar \
       /tmp/LICENSE /tmp/changelog.md . \
 && wget -O /usr/bin/yq https://github.com/mikefarah/yq/releases/download/${YQ_VER}/yq_linux_${YQ_ARCH} \
 && chmod 755 /usr/bin/yq \
 && rm -rf /tmp/*

VOLUME ["/config"]
EXPOSE 5076

# Keep version argument for runtime
ENV NZBHYDRA_VER=${NZBHYDRA_VER}

HEALTHCHECK --start-period=20s --timeout=5s \
    CMD wget -SO/dev/null "$(yq e '["http://",.main.host,":",.main.port,.main.urlBase,"/api/stats?apikey=",.main.apiKey]|join("")' /config/nzbhydra.yml)"

ENV LOGDIR=/config/logs

ENTRYPOINT ["/sbin/tini", "--", "su-exec", "--env"]
CMD mkdir -p ${LOGDIR} && \
    exec java -Xmx${MAXMEM} -DfromWrapper -noverify \
        -XX:TieredStopAtLevel=1 \
        -Xlog:gc:${LOGDIR}/gclog-$(date +"%F_%H-%M-%S").log \
        -Dspring.output.ansi.enabled=ALWAYS \
        -jar $NZBHYDRA_DIR/core-${NZBHYDRA_VER}-exec.jar \
        --datafolder /config
