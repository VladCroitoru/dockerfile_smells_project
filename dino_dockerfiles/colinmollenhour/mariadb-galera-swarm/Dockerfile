FROM mariadb:10.2

# Download blocked from http://www.quicklz.com/qpress-11-linux-x64.tar
COPY bin/qpress-11-linux-x64.tar /tmp/qpress.tar

RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
      curl \
      netcat \
      pigz \
      percona-toolkit \
      percona-xtrabackup \
      pv \
    && tar -C /usr/local/bin -xf /tmp/qpress.tar qpress \
    && chmod +x /usr/local/bin/qpress \
    && apt-get clean all && rm -rf /tmp/* /var/lib/apt/lists/*

COPY conf.d/*                /etc/mysql/conf.d/
COPY *.sh                    /usr/local/bin/
COPY bin/galera-healthcheck  /usr/local/bin/galera-healthcheck
COPY primary-component.sql   /

RUN set -ex ;\
    # Fix permissions
    chown -R mysql:mysql /etc/mysql ;\
    chmod -R go-w /etc/mysql ;\
    # Disable code that deletes progress file after SST
    sed -i 's#-p \$progress#-p \$progress-XXX#' /usr/bin/wsrep_sst_mariabackup ;\
    sed -i 's#-p \$progress#-p \$progress-XXX#' /usr/bin/wsrep_sst_xtrabackup

EXPOSE 3306 4444 4567 4567/udp 4568 8080 8081

HEALTHCHECK CMD /usr/local/bin/healthcheck.sh

ENV SST_METHOD=mariabackup

ENTRYPOINT ["start.sh"]
