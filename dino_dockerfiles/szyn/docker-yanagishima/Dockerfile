FROM openjdk:8u131-jre-alpine
LABEL maintainer "szyn <aqr.aqua@gmail.com>"

ENV VERSION=6.0

RUN apk add --no-cache unzip openssl bash && \
    cd /tmp && \
    wget https://bintray.com/artifact/download/wyukawa/generic/yanagishima-${VERSION}.zip && \
    unzip yanagishima-${VERSION}.zip -d /opt && \
    rm yanagishima-${VERSION}.zip && \
    sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

WORKDIR /opt/yanagishima-${VERSION}
COPY . .

EXPOSE 8080

CMD ["bash", "docker-entrypoint.sh"]
