FROM navikt/java:13
COPY init.sh /init-scripts/init.sh
COPY build/libs/event-test-producer-all.jar /app/app.jar
ENV JAVA_OPTS="-XX:MaxRAMPercentage=75 \
               -XX:+HeapDumpOnOutOfMemoryError \
               -XX:HeapDumpPath=/oom-dump.hprof"
ENV PORT=8080
EXPOSE $PORT
