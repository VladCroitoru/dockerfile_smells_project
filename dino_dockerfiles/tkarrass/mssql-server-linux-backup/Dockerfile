#
# tkarrass/mssql-server-linux-backup
#
# Extend Microsofts sql server docker image in order to 
# automate hourly backups to /backup

# Extend the original microsoft sql server docker image:
FROM microsoft/mssql-server-linux:2017-latest
MAINTAINER Thilo Karraß <tk@aurex.de>

# Let apt know there is no one in meatspace to ask any questions
ENV DEBIAN_FRONTEND noninteractive

# Add a script for backing up every single database to /backup/
ADD sql_backup.sh /usr/local/sbin/
RUN chmod +x /usr/local/sbin/sql_backup.sh

# Add a cronjob for executing beforementioned script regularly
RUN apt-get update \
 && apt-get -y install -qq apt-utils \
 && apt-get -y install -qq cron
ADD crontab /root/tmpcron
ADD runcron.sh /root/runcron.sh
RUN chmod +x /root/runcron.sh
RUN touch /var/log/cron.log

# Install supervisord in order to run cron alongside the sql server instance
RUN apt-get -y install -qq supervisor
ADD supervisor_cron.conf /etc/supervisor/conf.d/cron.conf
ADD supervisor_mssql.conf /etc/supervisor/conf.d/mssql.conf

EXPOSE 1433
CMD /usr/bin/supervisord -n
