FROM jpetazzo/dind

# docker config, see jpetazzo/dind
ENV DOCKER_DAEMON_ARGS -D
# include docker-compose
RUN curl -L https://github.com/docker/compose/releases/download/1.3.3/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
   && chmod +x /usr/local/bin/docker-compose

# install shellinabox and other missing features and cleanup
RUN apt-get update && apt-get -y install shellinabox vim nano \
    && rm -rf /var/lib/apt/lists; rm /tmp/*; apt-get purge

# add training user
RUN useradd -ms /bin/bash training ; \
    echo "training:training" | chpasswd ; \
    usermod -aG docker training;

# add start script
ADD start.sh .
RUN chmod +x start.sh

EXPOSE 4200

CMD ["./start.sh"]
