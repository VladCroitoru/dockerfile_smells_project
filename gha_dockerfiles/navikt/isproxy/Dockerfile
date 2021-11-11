FROM navikt/java:11
COPY build/libs/app.jar app.jar
ENV JAVA_OPTS="-Dlogback.configurationFile=logback.xml \
               -Dhttp.nonProxyHosts=*.adeo.no|*.preprod.local|*oera-q.local|*.oera.no"
