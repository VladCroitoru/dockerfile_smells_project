#original project:
#nimmis/docker-alpine-mariadb

FROM nimmis/alpine-micro

#deprecated
#MAINTAINER wrightie <wrightie@wrightie.eu>

#unused args
#ARG IMAGE_NAME
#ARG DOCKER_REPO
#ARG BUILD_DATE
#ARG VCS_REF

# fix labels
LABEL maintainer="wrightie <wrightie@wrightie.eu>" \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.name="MariaDB database"
      #org.label-schema.name="MariaDB database" \
      #org.label-schema.url="https://www.nimmis.nu" \
      #org.label-schema.build-date=$BUILD_DATE \
      #org.label-schema.vcs-ref=$VCS_REF \
      #org.label-schema.vcs-url="https://github.com/nimmis/docker-alpine-mariadb.git"

COPY root/. /


#defaulting locale to it_IT
ENV LANG="it_IT.UTF-8" \
    LC_ALL="it_IT.UTF-8" \
    LANGUAGE="it_IT.UTF-8"

RUN apk update && apk upgrade && \
#
    # Make info file about this build
    #mkdir -p /etc/BUILDS/ && \
    #printf "Build of %s, date: %s\n" $(echo $IMAGE_NAME | sed 's#^.*io/##')  `date -u +"%Y-%m-%dT%H:%M:%SZ"` > /etc/BUILDS/$(echo $DOCKER_REPO | awk -F '/' '{print $NF}') && \
#
    # add mariadb server and client
    apk add mariadb mariadb-client && \
#
    # clear cache
    rm -rf /var/cache/apk/*

VOLUME /data

EXPOSE 3306