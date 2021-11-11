FROM java:7

ENV STASH_HOME     /var/atlassian/stash
ENV STASH_INSTALL  /opt/atlassian/stash

RUN set -x \
    && apt-get update --quiet \
    && apt-get install --quiet --yes --no-install-recommends libtcnative-1 git-core xmlstarlet \
    && apt-get clean 

# Use the default unprivileged account. This could be considered bad practice
# on systems where multiple processes end up being executed by 'daemon' but
# here we only ever run one process anyway.
USER daemon:daemon

# Expose default HTTP connector port.
EXPOSE 7990 7999

CMD ["/opt/atlassian/stash/bin/start-stash.sh", "-fg"]