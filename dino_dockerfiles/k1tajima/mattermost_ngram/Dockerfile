ARG TAG=5.7.2
FROM mattermost/mattermost-preview:${TAG}
LABEL maintainer="https://qiita.com/k1tajima"

ARG TAG
RUN echo "k1tajima/mattermost_ngram:${TAG}" > image_tag \
    && echo "FROM mattermost/mattermost-preview:${TAG}" >> image_tag \
    && cat image_tag

ENV MATTERMOST_HOME=/mm/mattermost
VOLUME ["$MATTERMOST_HOME/config","$MATTERMOST_HOME/mattermost-data"]

# Install wait-for-it.
# See https://docs.docker.com/compose/startup-order/
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Set default character set to UTF8 on MySQL.
COPY my.cnf /etc/

# Store initial config
WORKDIR $MATTERMOST_HOME
RUN mkdir config_init ; \
    cp -rp config/* config_init/ ; \
    chmod 775 config_init ; \
    chmod 664 config_init/* ; \
    chown -R 1000:1000 config_init

# Activate N-gram parser on MySQL to search a sentence in Japanese.
WORKDIR /mm
COPY docker-entry_ngram.sh .
COPY reindex-ngram.sh .
RUN chmod +x docker-entry_ngram.sh reindex-ngram.sh
ENTRYPOINT ["/mm/docker-entry_ngram.sh"]

# Set Current Directory
WORKDIR $MATTERMOST_HOME
