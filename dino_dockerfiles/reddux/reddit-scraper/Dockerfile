FROM python:3

ADD config.py /
ADD bot.py /
ADD run.sh /

RUN pip install requests praw pyrebase

# Cron
ADD run.sh /etc/cron.hourly/reddit-scraper
