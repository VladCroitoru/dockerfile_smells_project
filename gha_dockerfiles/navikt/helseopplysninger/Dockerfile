FROM ghcr.io/navikt/hops-build AS build
COPY . .
ARG project
RUN gradle apps:${project}:shadowJar --no-daemon --no-build-cache

FROM navikt/java:17
COPY --from=build /home/gradle/apps/*/build/libs/*.jar app.jar
