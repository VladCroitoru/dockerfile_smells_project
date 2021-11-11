FROM jruby:9-alpine

MAINTAINER Tokyo Home SOC <github@homesoc.tokyo>

# Environment variable
ARG TIMEZONE=Asia/Tokyo
ARG JOLOKIA_VERSION=1.3.5

RUN \
    # TIMEZONE
       apk add --no-cache \
        tzdata \
    && cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
    && apk del tzdata \
    \
    && gem install norikra --no-ri --no-rdoc \
    && apk add --no-cache --virtual .jolokia-deps \
            curl \
    && mkdir -p /opt/jolokia/ \
    && curl -fSL https://repo1.maven.org/maven2/org/jolokia/jolokia-jvm/${JOLOKIA_VERSION}/jolokia-jvm-${JOLOKIA_VERSION}-agent.jar \
        -o /opt/jolokia/jolokia-jvm-agent.jar \
    && apk del .jolokia-deps

EXPOSE 26571/tcp 26578/tcp 8778/tcp
VOLUME /var/norikra
ENTRYPOINT ["norikra", "start", "-javaagent:/opt/jolokia/jolokia-jvm-agent.jar=port=8778,host=0.0.0.0", "-Xms256m", "-Xmx256m","--stats=/var/norikra/stats.json", "--dump-stat-interval=60"]