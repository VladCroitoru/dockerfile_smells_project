FROM quay.io/evryfs/base-java-service:java11-20211026
LABEL maintainer="David J. M. Karlsen <david.karlsen@tietoevry.com>"
ARG VERSION
COPY maven/ /app/
# JAVA_OPTS can be used to pass any additional system properties from env vars
CMD ["bash", "-c", "java ${DEFAULT_JAVA_OPTIONS} ${JAVA_OPTS} -jar spring-boot-admin.jar"]
