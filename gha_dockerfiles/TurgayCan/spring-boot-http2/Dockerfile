# Usage is explained in README.md file
FROM hirokimatsumoto/alpine-openjdk-11
MAINTAINER info@turgaycan.dev

VOLUME /tmp

VOLUME /logs

ENV TZ=Europe/Istanbul

RUN apk add --no-cache tini \
  && apk add --no-cache tzdata \
  && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
  && echo "${TZ}" > /etc/timezone

# JAR_FILE argument is provided by build.sh
ARG JAR_FILE
ADD ${JAR_FILE} /app.jar

ENTRYPOINT [ "/sbin/tini", "--", "sh", "-c", "java ${JAVA_OPTS} -Djava.security.egd=file:/dev/./urandom -jar /app.jar ${APP_OPTS}" ]
