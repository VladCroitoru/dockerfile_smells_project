FROM navikt/java:13-appdynamics
COPY init.sh /init-scripts/init.sh
COPY build/libs/dittnav-periodic-metrics-reporter-all.jar /app/app.jar
ENV JAVA_OPTS="-XX:MaxRAMPercentage=75 \
               -XX:+HeapDumpOnOutOfMemoryError \
               -XX:HeapDumpPath=/oom-dump.hprof"
ENV PORT=8080
EXPOSE $PORT
