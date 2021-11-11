FROM maven:3.5-jdk-8-alpine

RUN apk -U add git \
    && mkdir /build \
    && cd /build \
    # Build master of docker-java
        && git clone https://github.com/cybe/docker-java.git \
        && cd /build/docker-java \
        && export VERSION_DOCKER_JAVA="$(git rev-parse --abbrev-ref HEAD)-$(git rev-parse --short HEAD)" \
        && mvn -P'!docker-java-analyses' org.codehaus.mojo:versions-maven-plugin:2.4:set -DnewVersion=${VERSION_DOCKER_JAVA} \
        && mvn -DskipTests -P'!docker-java-analyses' install \
    # Build master of yet-another-docker-plugin with master of docker-java as dependency
        && cd /build \
        && git clone https://github.com/KostyaSha/yet-another-docker-plugin.git \
        && cd yet-another-docker-plugin \
        && mvn -pl yet-another-docker-java org.codehaus.mojo:versions-maven-plugin:2.4:use-dep-version -DdepVersion=${VERSION_DOCKER_JAVA} -Dincludes=com.github.docker-java:docker-java \
        && export VERSION_YADP="1.0.3-SPU-$(git rev-parse --abbrev-ref HEAD)-$(git rev-parse --short HEAD)" \
        && mvn org.codehaus.mojo:versions-maven-plugin:2.4:set -DnewVersion=${VERSION_YADP} \
        && mvn -pl yet-another-docker-java org.codehaus.mojo:versions-maven-plugin:2.4:set -DnewVersion=${VERSION_YADP} \
        && mvn -DskipTests -Denforcer.skip=true install \
        && cp /root/.m2/repository/com/github/kostyasha/yet-another-docker/yet-another-docker-plugin/**/yet-another-docker-plugin-*.hpi / \
    # Cleanup
        && cd / \
        && apk del git \
        && rm -rf /build \
        && rm -rf /root/.m2/repository \
    # Upload
        && FILENAME="$(ls yet-another-docker-plugin-*.hpi)" \
        && echo "Uploading ${FILENAME} to transfer.sh" \
        && echo "Download: $(curl --upload-file /${FILENAME} https://transfer.sh/${FILENAME})"
