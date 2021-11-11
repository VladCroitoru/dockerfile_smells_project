FROM navikt/java:11
COPY ./target/*shaded.jar "app.jar"
ENV JAVA_OPTS="-XX:MaxRAMPercentage=75"
