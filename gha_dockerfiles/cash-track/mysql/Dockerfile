# Periodic "Packets out of order" bug.
# Temporary downgrading build to 8.0.23. Awaiting for 8.0.27+
# Unable to downgrade, keeping in 8.0.26.
#
# See: https://bugs.php.net/bug.php?id=81335&edit=1
FROM mysql:8.0.26

RUN ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo UTC > /etc/timezone

RUN chown -R mysql:root /var/lib/mysql/

ADD my.cnf /etc/mysql/conf.d/my.cnf

CMD ["mysqld"]

EXPOSE 3306