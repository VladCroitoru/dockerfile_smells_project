FROM chapeter/alpine
MAINTAINER Chad Peterson, chapeter@cisco.com

RUN apk add gcc

WORKDIR /home
COPY . sparkdaily/
WORKDIR sparkdaily

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo '0 5 * * * /usr/bin/python /home/sparkdaily/sparkdaily.py >> /var/log/cron.log 2>&1' > crontab
RUN chmod 0644 crontab
RUN cp crontab /etc/crontabs/root
RUN touch /var/log/cron.log

EXPOSE 5000

CMD crond && python healthcheck.py
