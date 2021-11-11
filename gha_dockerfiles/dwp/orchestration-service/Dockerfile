FROM openjdk:14-alpine
ENV APP_NAME=orchestration-service
ENV APP_HOME=/opt/${APP_NAME}
ENV USER=os_user
RUN mkdir ${APP_HOME} ${APP_HOME}/keystore
WORKDIR ${APP_HOME}
COPY build/libs/*.jar ./${APP_NAME}.jar
RUN addgroup -S ${USER} && adduser -S ${USER} && \
        chown -R ${USER}.${USER} . && \
        chmod +x ./${APP_NAME}.jar && ls -l && pwd

COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
