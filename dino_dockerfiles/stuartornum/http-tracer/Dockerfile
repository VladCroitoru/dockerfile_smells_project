FROM python:2.7.13

WORKDIR /srv/
ADD requirements.txt /srv
RUN pip install -r requirements.txt

ADD . /srv

EXPOSE 5000
ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
