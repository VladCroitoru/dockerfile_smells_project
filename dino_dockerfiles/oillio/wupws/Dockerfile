FROM ubuntu

RUN apt-get -q update && apt-get install -qy --force-yes jq wget cron

ADD ./wu-pws.sh /wu-pws.sh
RUN chmod a+x /wu-pws.sh
ADD ./start.sh /start.sh
RUN chmod a+x /start.sh

ADD ./crontab /etc/crontab
RUN chmod a+x /etc/crontab

CMD ["/start.sh"]
