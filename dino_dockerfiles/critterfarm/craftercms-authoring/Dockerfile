FROM openjdk:8-jdk

LABEL maintainer="geksiong@gmail.com"
LABEL description="Non-official Crafter CMS Authoring module"

ENV CRAFTER_AUTHOR_DOWNLOAD https://s3.amazonaws.com/downloads.craftercms.org/3.0.8/social/crafter-cms-authoring.tar.gz
ENV CRAFTER_AUTHOR_HOME /opt/crafter-authoring

RUN apt-get update && apt-get install -y --no-install-recommends lsof bc \
    && apt-get clean && rm -rf /var/lib/apt/lists/ \
    && useradd -c 'Crafter Author' -m -d ${CRAFTER_AUTHOR_HOME} -s /bin/bash crafter
USER crafter
WORKDIR ${CRAFTER_AUTHOR_HOME}
RUN wget https://s3.amazonaws.com/downloads.craftercms.org/3.0.8/social/crafter-cms-authoring.tar.gz \
    && tar xvzf crafter-cms-authoring.tar.gz \
    && rm crafter-cms-authoring.tar.gz
WORKDIR ${CRAFTER_AUTHOR_HOME}/crafter/bin
RUN mkdir mongodb \
    && cd mongodb \
    && java -jar ../craftercms-utils.jar download mongodb \
    && tar xvf mongodb.tgz --strip 1 \
    && rm mongodb.tgz

EXPOSE 8080
VOLUME ["data", "logs"]
CMD ["sh","-c","./startup.sh && tail -f /dev/null"]
