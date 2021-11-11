FROM maven:3.3-jdk-8

ENV JAVA_TOOL_OPTIONS="-Xmx350m -Xss512k -Dfile.encoding=UTF-8 -Xss512k -XX:+UseCompressedOops -Duser.timezone=Europe/Paris"

WORKDIR /app/build
ADD . /app/build
RUN mvn --errors --activate-profiles docker --define maven.test.skip=true clean package && \
    mv -v target/plt.jar /app/plt.jar && \
    rm -rf /app/build

WORKDIR /app
ENTRYPOINT ["java", "-Dspring.profiles.active=heroku", "-jar", "/app/plt.jar"]
