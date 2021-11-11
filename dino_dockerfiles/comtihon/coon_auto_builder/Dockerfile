FROM comtihon/alpine_erlang

RUN apk update  \
    && apk add python3 \
    && pip3 install enot

RUN mkdir -p ${HOME}/.config/enot

COPY docker/global_config.json ${HOME}/.config/enot/
COPY src src
COPY build.gradle .
COPY settings.gradle .
COPY gradlew .
COPY gradle gradle
RUN ./gradlew build -x test_integration
RUN cp build/libs/enot_auto_builder-*.jar ${HOME}/app.jar

ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar ${HOME}/app.jar