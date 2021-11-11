FROM jupyter/all-spark-notebook:c54800018c2c
LABEL maintainer = "msommer@iplus1.de"

USER root

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get update && apt-get install -y vim less netcat pwgen curl libsasl2-dev libldap2-dev libssl-dev docker sqlite3 && apt-get clean

RUN apt-get update && apt-get install -yq cron locales daemontools jq

ADD jobengine/requirements.txt /tmp/
RUN bash -c "mkdir -p /var/www/jobengine/ && cd /var/www/jobengine/ && conda create -y --prefix ./venv  python=3.8 && source activate ./venv ; conda install --file /tmp/requirements.txt"

ADD jobengine /var/www/jobengine

ADD start.sh /start.sh
ADD wrapper.sh /jobengine/wrapper.sh
ADD update_job_states.sh /jobengine/update_job_states.sh
ADD common /common

RUN chmod +x /start.sh
RUN chmod +x /jobengine/wrapper.sh
RUN chmod +x /jobengine/update_job_states.sh

EXPOSE 8010

CMD ["/start.sh"]
