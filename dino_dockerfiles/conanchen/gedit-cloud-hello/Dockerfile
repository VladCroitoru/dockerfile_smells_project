FROM frolvlad/alpine-oraclejdk8
LABEL maintainer="https://github.com/conanchen"
VOLUME /tmp
ARG JAR_FILE
ADD ${JAR_FILE} app.jar
ENV SPRING_APPLICATION_JSON='\
{"gedit": {\
    "docker":{"enabled":true},\
    "cloud": {\
        "config": {\
            "server": {\
                "git": {\
                    "uri": "/var/lib/gedit-cloud/config-repo",\
                    "clone-on-start": true \
                    }\
                }\
            }\
        }\
    }\
}'
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
EXPOSE 8088 8980
