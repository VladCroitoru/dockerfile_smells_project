#############################
#   Builder
#############################
FROM ghcr.io/icgc-argo/graalvm-docker-image:java11-21.2.0-extras-1.0.0 as builder
WORKDIR /usr/src/app
ADD . .
RUN ./mvnw clean package -DskipTests

#############################
#   Server
#############################
FROM ghcr.io/icgc-argo/graalvm-docker-image:java11-21.2.0-extras-1.0.0

ENV APP_HOME /srv
ENV APP_USER wfuser
ENV APP_UID 9999
ENV APP_GID 9999

WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/target/workflow-graph-node-*.jar $APP_HOME/workflow-graph-node.jar

RUN groupadd -g $APP_GID $APP_USER \
    && useradd -u $APP_UID -g $APP_USER $APP_USER \
    && chown -R $APP_UID:$APP_GID $APP_HOME

USER $APP_UID

CMD ["java", "-ea", "-jar", "/srv/workflow-graph-node.jar"]
EXPOSE 8080/tcp
