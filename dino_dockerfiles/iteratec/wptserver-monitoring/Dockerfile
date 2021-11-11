FROM python:alpine

RUN mkdir -p /opt/wptserver-monitoring/conf

ADD monitoring.py /opt/wptserver-monitoring/monitoring.py
ADD conf.json /opt/wptserver-monitoring/conf/conf.json

RUN touch crontab.tmp \
    && echo '*/5 * * * * /usr/local/bin/python /opt/wptserver-monitoring/monitoring.py' > crontab.tmp \
    && crontab crontab.tmp \
    && rm -rf crontab.tmp
CMD ["crond", "-f", "-d", "8"]
