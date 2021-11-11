FROM python:3.6
MAINTAINER foo@bar.org

RUN pip install python-cloudflare
ADD purge.sh /
RUN chmod +x /purge.sh
