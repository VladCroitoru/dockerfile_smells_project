FROM       debian:buster-slim

LABEL      maintainer="SlothDS" \
           maintainer.mail="sloth@devils.su" \
           maintainer.git="https://github.com/slothds"

ENV        DEBIAN_FRONTEND=noninteractive

COPY       rootfs /

RUN        mkdir -p /usr/share/man/man1 && touch /usr/share/man/man1/sh.1.gz && \
           apt-get update && apt-get -y upgrade && \
           { \
               which gpg \
               || apt-get -y install --no-install-recommends gnupg2 \
               || apt-get -y install --no-install-recommends gnupg; \
           } && \
           { \
               gpg --version | grep -q '^gpg (GnuPG) 1\.' \
               || apt-get -y install --no-install-recommends dirmngr; \
           } && \
           apt-get -y install --reinstall --no-install-recommends \
                              tzdata locales apt-utils \
                              supervisor cron && \
           apt-get -y autoremove && apt-get -y autoclean && \
           apt-get -y clean && apt-get -y clean all && \
           rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*
RUN        locale-gen en_US.UTF-8 && \
           groupadd -g 10001 runner && \
           useradd -u 10001 -g 10001 -G users -md /opt/runner -s /bin/false runner && \
           mkdir -p /exec/env.d /exec/init.d && \
           chown -R runner:runner /exec && chmod -R 775 /exec

ENTRYPOINT ["/entrypoint.sh"]

STOPSIGNAL SIGTERM
