FROM python:3.6

WORKDIR /srv
ADD requirements.txt /srv/
RUN pip install -r requirements.txt

COPY scrapyd.conf /etc/scrapyd/scrapyd.conf

CMD ["/bin/sh", "-c", "rm -Rf twistd.pid && scrapyd"]