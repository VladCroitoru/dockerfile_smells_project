FROM gradle:jdk
COPY \
 build.gradle build.properties gradle.properties ./
COPY \
 src ./src
RUN gradle installDist
CMD ["/home/gradle/build/install/gradle/bin/gradle"]
