# SOLDAT SERVER DOCKER
# ---------------------------------------------
FROM 32bit/debian:latest
LABEL maintainer="Raymond Piller <VertigoRay@vertigion.com>"

# update debian packages
RUN apt-get update && \
    apt-get -y --force-yes upgrade && \
    apt-get -y --force-yes install wget unzip && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /soldat

# copy soldat config
ADD ./config/ /soldat/

# add user soldat
RUN useradd -ms /bin/bash soldat && \
    chown -R soldat:soldat /soldat

USER soldat
EXPOSE 23073
EXPOSE 23083

CMD /bin/bash -c "source /soldat/setup.sh"
