FROM gradle:3.5-jdk-alpine
ENV RCLONE_VERSION v1.36

# The gradle image runs under the user "gradle", but when you run as gradle, the gradle cache directory is inside a
# volume, which results in dependencies being wiped on every step in the docker build.
USER root

# There is no point in running the gradle daemon, as it would be stopped by docker on every step in the build anyway.
ENV GRADLE_OPTS -Dorg.gradle.daemon=false

RUN apk --no-cache add openssl
RUN wget https://github.com/ncw/rclone/releases/download/$RCLONE_VERSION/rclone-$RCLONE_VERSION-linux-amd64.zip && \
    unzip rclone-$RCLONE_VERSION-linux-amd64.zip rclone-$RCLONE_VERSION-linux-amd64/rclone && \
    mv rclone-$RCLONE_VERSION-linux-amd64/rclone /usr/local/bin/ && \
    rmdir rclone-$RCLONE_VERSION-linux-amd64 && \
    rm rclone-$RCLONE_VERSION-linux-amd64.zip

# Working directory
RUN mkdir /kubernetes-volume-backup
WORKDIR /kubernetes-volume-backup

# Dependencies
COPY build.gradle .
RUN gradle downloadDependencies

# Compilation
COPY . .
RUN gradle jar

ENTRYPOINT ["./entrypoint.sh"]
CMD ["java", "-jar", "build/libs/volume-backup.jar"]
