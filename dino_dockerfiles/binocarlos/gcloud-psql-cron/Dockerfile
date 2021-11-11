# a dockerfile with:
#  * the gcloud client
#  * a storage service account key
#  * psql
FROM google/cloud-sdk
MAINTAINER kaiyadavenport@gmail.com
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' >> /etc/apt/sources.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update
RUN apt-get install -y python-setuptools postgresql-9.6
RUN easy_install pip
RUN pip install https://bitbucket.org/dbenamy/devcron/get/tip.tar.gz
ADD ./crontab /cron/crontab
ADD ./run.sh /app/run.sh
ADD ./backup.sh /app/backup.sh
RUN chmod a+x /app/run.sh
RUN chmod a+x /app/backup.sh
ENTRYPOINT ["/app/run.sh"]