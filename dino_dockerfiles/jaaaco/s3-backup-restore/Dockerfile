FROM debian:jessie-slim

RUN apt-get update && apt-get install -y cron python-pip
RUN pip install awscli

ADD command /
RUN chmod +x command
VOLUME /var/log/
CMD /command cron
