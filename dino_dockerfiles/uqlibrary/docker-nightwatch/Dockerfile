FROM node:latest

USER root

RUN \
    npm install -g nightwatch python curl --ignore-scripts --unsafe-perm --loglevel info && \
    curl -o /usr/local/bin/jq http://stedolan.github.io/jq/download/linux64/jq && \
    chmod +x /usr/local/bin/jq && \
    groupadd -r docker && \
    useradd -r -g docker docker

COPY nightwatch.sh /opt/nightwatch.sh
RUN chmod +x /opt/nightwatch.sh

CMD /opt/nightwatch.sh
