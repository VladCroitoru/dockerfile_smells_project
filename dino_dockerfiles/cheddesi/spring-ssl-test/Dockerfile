FROM cheddesi/soejre
VOLUME /tmp
ADD app.jar app.jar
ADD dev_server_identity.jks dev_server_identity.jks
ADD application.yml application.yml
ENV JAVA_OPTS=""
ENV FILE_PATH=/application.yml
EXPOSE 443
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app.jar --spring.config.location=$FILE_PATH"]
