# Build web (javascript & css)
FROM node:15.11.0-stretch AS build-web
WORKDIR /app
COPY --chown=1000:1000 web/src/less src/less
COPY --chown=1000:1000 web/src/scripts src/scripts
COPY --chown=1000:1000 web/.bowerrc .
COPY --chown=1000:1000 web/bower.json .
COPY --chown=1000:1000 web/Gruntfile.js .
COPY --chown=1000:1000 web/package.json .
COPY --chown=1000:1000 web/package-lock.json .
RUN npm install
RUN node_modules/.bin/bower install --allow-root
RUN node_modules/.bin/grunt

# Build Java
FROM gradle:7.2.0-jdk16 AS build-java
WORKDIR /app
COPY --chown=gradle:gradle java/src src/
COPY --chown=gradle:gradle java/build.gradle .
COPY --chown=gradle:gradle java/lombok.config .
RUN gradle bootJar
WORKDIR build/libs
RUN java -Djarmode=layertools -jar app.jar extract

# Create production image
FROM openjdk:16-alpine AS prod
LABEL maintainer="oss@ceh.ac.uk"
RUN apk --no-cache add curl
RUN addgroup -g 1001 -S spring && adduser -u 1001 -S spring -G spring
RUN mkdir -p /var/ceh-catalogue/datastore /var/ceh-catalogue/dropbox /var/ceh-catalogue/mapfiles /var/ceh-catalogue/tdb /var/upload/datastore
WORKDIR /app
COPY schemas /opt/ceh-catalogue/schemas
COPY  --from=build-java /app/build/libs/dependencies/ ./
COPY --from=build-java /app/build/libs/spring-boot-loader/ ./
COPY --from=build-java /app/build/libs/snapshot-dependencies/ ./
COPY --from=build-java /app/build/libs/application/ ./
COPY templates /opt/ceh-catalogue/templates
COPY --from=build-web /app/src/css /opt/ceh-catalogue/static/css
COPY web/src/img /opt/ceh-catalogue/static/img
COPY --from=build-web /app/src/scripts/main-out.js /opt/ceh-catalogue/static/scripts/main-out.js
COPY --from=build-web /app/src/scripts/upload-out.js /opt/ceh-catalogue/static/scripts/upload-out.js
COPY --from=build-web /app/src/vendor/font-awesome-5/webfonts /opt/ceh-catalogue/static/vendor/font-awesome-5/webfonts
COPY --from=build-web /app/src/vendor/requirejs/require.js /opt/ceh-catalogue/static/vendor/requirejs/require.js
RUN chown spring:spring -R /app \
 && chown spring:spring -R /opt/ceh-catalogue \
 && chown spring:spring -R /var/ceh-catalogue \
 && chown spring:spring -R /var/upload
VOLUME ["/var/ceh-catalogue/datastore", "/var/ceh-catalogue/dropbox", "/var/ceh-catalogue/mapfiles", "/var/upload/datastore"]
EXPOSE 8080 8081
USER spring
ENTRYPOINT ["java", "org.springframework.boot.loader.JarLauncher"]
HEALTHCHECK --start-period=30s CMD curl --no-progress-meter --output - --fail http://localhost:8081/actuator/health || exit 1

# Create Datalabs image
FROM prod as datalabs
USER root

# Create resources for development only
FROM alpine/git:v2.30.1 AS datastore
COPY fixtures/datastore/REV-1 /datastore
WORKDIR /datastore
RUN git config --global init.defaultBranch main \
    && git init \
    && git config user.email "test@example.com" \
    && git config user.name "test" \
    && git add -A \
    && git commit -m "data loading"

# Development image
FROM prod AS dev
COPY --chown=spring:spring --from=datastore /datastore /var/ceh-catalogue/datastore
USER root
RUN apk --no-cache add git vim
USER spring

