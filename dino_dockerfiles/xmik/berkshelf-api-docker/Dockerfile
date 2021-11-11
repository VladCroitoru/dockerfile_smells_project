FROM ruby:2.2.3-slim
MAINTAINER Ewa Czechowska <ewa@ai-traders.com>

RUN mkdir /scripts
COPY scripts /scripts 
ENV DEBIAN_FRONTEND=noninteractive

# add linux user: berkshelf
RUN useradd berkshelf -d /home/berkshelf -s /bin/bash -u 262 --system && \
    mkdir -p /home/berkshelf/.berkshelf/api-server && \
    mkdir -p /home/berkshelf/.chef && \
    chown berkshelf:berkshelf -R /home/berkshelf/ && \
    mv /scripts/run_berks_api.sh /usr/bin/run_berks_api.sh && \
    chmod 755 /usr/bin/run_berks_api.sh

# install berkshelf, make bundler invokable by berkshelf linux user (symlink)
# install libarchive-dev to avoid error:
# "Could not open library 'libarchive.so': libarchive.so: cannot open shared object file:
# No such file or directory"
RUN apt-get update  && \
    apt-get install -y nano procps build-essential libarchive-dev && \
    cd /scripts && bundle install && \
    ln -s /usr/local/bundle/bin/bundle /usr/bin/bundle

# clean
RUN apt-get purge -y build-essential && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/* && \
    rm -rf /var/lib/apt/lists/*
# do not remove /scripts, there are Gemfiles to be used on each start up

# add image metadata
RUN touch /etc/docker_metadata.txt && \
    VERSION=$(cat /scripts/version.txt) && \
    echo -e "base_image_name = ruby\n\
base_image_tag = 2.2.3-slim\n\
this_image_name = xmik/berkshelf-api-docker\n\
this_image_tag = ${VERSION}\n\
" >> /etc/docker_metadata.txt


EXPOSE 26200
ENTRYPOINT ["/bin/bash", "-c"]
# Run as user: berkshelf but still enable logging as root to a running
# container with "docker exec", thus do not add: "USER berkshelf".
CMD ["/usr/bin/run_berks_api.sh"]