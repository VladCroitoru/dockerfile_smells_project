FROM openjdk:8-jdk-alpine
ARG JAR_FILE=core-connector/target/*.jar
COPY ${JAR_FILE} app.jar
ENV MLCONN_OUTBOUND_ENDPOINT=http://simulator:3003
ENV DFSP_NAME="DFSP CO. LTD."
ENV DFSP_HOST="https://localhost/api"
ENV DFSP_USERNAME=username
ENV DFSP_PASSWORD=password
ENV DFSP_AUTH_CLIENT_ID=clientId
ENV DFSP_AUTH_CLIENT_SECRET=clientSecret
ENV DFSP_AUTH_GRANT_TYPE=grantType
ENV DFSP_AUTH_SCOPE=scope
ENV DFSP_AUTH_ENCRYPTED_PASS=false
ENV DFSP_AUTH_TENANT_ID=tenantId
ENTRYPOINT ["java", "-Dml-conn.outbound.host=${MLCONN_OUTBOUND_ENDPOINT}", "-Ddfsp.name=${DFSP_NAME}", "-Ddfsp.host=${DFSP_HOST}", "-Ddfsp.username=${DFSP_USERNAME}", "-Ddfsp.password=${DFSP_PASSWORD}", "-Ddfsp.scope=${DFSP_AUTH_SCOPE}", "-Ddfsp.client-id=${DFSP_AUTH_CLIENT_ID}", "-Ddfsp.client-secret=${DFSP_AUTH_CLIENT_SECRET}", "-Ddfsp.grant-type=${DFSP_AUTH_GRANT_TYPE}", "-Ddfsp.is-password-encrypted=${DFSP_AUTH_ENCRYPTED_PASS}", "-Ddfsp.tenant-id=${DFSP_AUTH_TENANT_ID}", "-jar", "/app.jar"]
EXPOSE 3003