#
# Nodejs + npm base install
# https://registry.hub.docker.com/_/node/
#
FROM node:4
MAINTAINER Inaki Anduaga <inaki@inakianduaga.com>

#
# Install supervisor
#
RUN apt-get update && apt-get upgrade -y && \
    apt-get -y install supervisor && \
    apt-get clean && apt-get autoremove -y

#
# Clone doorman repo and initialize npm packages
#
RUN apt-get -y --no-install-recommends install git  && \
    git clone --single-branch --branch master https://github.com/telor/doorman.git && \
    cd /doorman && \
    npm install

#
# Add doorman configuration
#
COPY conf/doorman/conf.js /doorman/conf.js

EXPOSE 8085
WORKDIR /doorman
VOLUME /config

#
# Supervisor startup scripts (also includes nginx)
#
ADD conf/supervisor/ /etc/supervisor/conf.d/
ADD scripts/ /scripts/
RUN chmod 755 /scripts/*.sh

# Default command
CMD ["/scripts/start.sh"]
