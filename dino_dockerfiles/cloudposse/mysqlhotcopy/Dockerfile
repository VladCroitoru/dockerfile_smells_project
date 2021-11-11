FROM cloudposse/mysql
WORKDIR /opt
ENV MYSQL_HOST localhost

RUN apt-get update && \
    apt-get -y install rsync git libdbd-mysql libdbd-mysql-perl && \
    apt-get clean && \
    git clone https://github.com/osterman/mysqlhotcopy.git /opt/mysqlhotcopy

ENTRYPOINT ["/opt/mysqlhotcopy/mysqlhotcopy"]

CMD --debug  --allowold --flushlog --method=rsync --user=root --password=$MYSQL_ROOT_PASSWORD --host=$MYSQL_HOST $MYSQL_DATABASE $MYSQL_BACKUPS
