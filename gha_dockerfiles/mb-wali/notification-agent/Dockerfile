FROM clojure:lein-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache git

RUN ln -s "/usr/bin/java" "/bin/notification-agent"

COPY project.clj /usr/src/app/
RUN lein deps

COPY conf/main/logback.xml /usr/src/app/
COPY . /usr/src/app

RUN lein uberjar && \
    cp target/notification-agent-standalone.jar .

ENTRYPOINT ["notification-agent", "-Dlogback.configurationFile=/etc/iplant/de/logging/notificationagent-logging.xml", "-cp", ".:notification-agent-standalone.jar", "notification_agent.core"]
CMD ["--help"]

ARG git_commit=unknown
ARG version=unknown
ARG descriptive_version=unknown

LABEL org.cyverse.git-ref="$git_commit"
LABEL org.cyverse.version="$version"
LABEL org.cyverse.descriptive-version="$descriptive_version"
LABEL org.label-schema.vcs-ref="$git_commit"
LABEL org.label-schema.vcs-url="https://github.com/cyverse-de/notification-agent"
LABEL org.label-schema.version="$descriptive_version"
