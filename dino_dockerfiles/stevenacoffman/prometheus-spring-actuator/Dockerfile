FROM openjdk:8-jre-alpine

RUN apk add --no-cache tini

ARG JAR_FILE
ENV JAR_FILE spring-boot.jar

ENV SERVER_PORT=8080
ENV DEBUG_PORT=8000
ENV JMX_PORT=9010
ENV APP_HOME /app
ENV SPRING_BOOT_USER spring-boot
ENV SPRING_BOOT_GROUP spring-boot

WORKDIR $APP_HOME
COPY assets/entrypoint.sh $APP_HOME/entrypoint.sh

# Is this necessary?
VOLUME /tmp

RUN addgroup -S $SPRING_BOOT_USER && \
  adduser -S -g $SPRING_BOOT_GROUP $SPRING_BOOT_USER && \
  chmod 555 $APP_HOME/entrypoint.sh

EXPOSE $SERVER_PORT
EXPOSE $DEBUG_PORT
EXPOSE $JMX_PORT

USER $SPRING_BOOT_USER
# Add Maven dependencies (not shaded into the artifact; Docker-cached)
ADD target/lib $APP_HOME/lib
ADD target/${JAR_FILE} $APP_HOME/${JAR_FILE}

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["./entrypoint.sh"]
