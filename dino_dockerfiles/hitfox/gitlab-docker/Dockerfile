FROM gitlab/gitlab-ce:8.8.4-ce.0

# install AWS client
RUN pip install awscli --ignore-installed six

# install db compatible postgres client version
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository "deb https://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main"
RUN wget --quiet -O - https://postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
RUN apt-get update
RUN apt-get -y install postgresql-client-9.4
RUN mv /opt/gitlab/embedded/bin/pg_dump /opt/gitlab/embedded/bin/pg_dump.old
RUN mv /opt/gitlab/embedded/bin/psql /opt/gitlab/embedded/bin/psql.old
RUN ln -s /usr/lib/postgresql/9.4/bin/pg_dump /usr/lib/postgresql/9.4/bin/psql /opt/gitlab/embedded/bin/

# install cron job to run backups
ADD crontab /etc/crontab
ADD backup.sh /
ADD restore.sh /
ADD start_services.sh /

CMD ["/start_services.sh"]
