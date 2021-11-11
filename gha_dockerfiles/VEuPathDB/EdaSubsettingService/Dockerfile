# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Build Service & Dependencies
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
FROM veupathdb/alpine-dev-base:jdk-15 AS prep

LABEL service="eda-subsetting-build"

ARG GITHUB_USERNAME
ARG GITHUB_TOKEN

WORKDIR /workspace
RUN jlink --compress=2 --module-path /opt/jdk/jmods \
       --add-modules java.base,java.net.http,java.security.jgss,java.logging,java.xml,java.desktop,java.management,java.sql,java.naming \
       --output /jlinked \
    && apk add --no-cache git sed findutils coreutils make npm curl gawk \
    && git config --global advice.detachedHead false

ENV DOCKER=build
COPY makefile .

RUN make install-dev-env

COPY . .

RUN mkdir -p vendor \
    && cp -n /jdbc/* vendor \
    && echo Installing Gradle \
    && ./gradlew dependencies --info --configuration runtimeClasspath \
    && make jar

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Run the service
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
FROM foxcapades/alpine-oracle:1.3

LABEL service="eda-subsetting"

ENV JAVA_HOME=/opt/jdk \
    PATH=/opt/jdk/bin:$PATH

COPY --from=prep /jlinked /opt/jdk
COPY --from=prep /workspace/build/libs/service.jar /service.jar

CMD java -jar /service.jar
