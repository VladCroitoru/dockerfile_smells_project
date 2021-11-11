FROM python:3.5

RUN apt-get update

COPY src/requirements.txt /
RUN pip install -r requirements.txt


COPY src /srv/

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

RUN mkdir /data/ && chown www-data:www-data /data/

USER www-data

WORKDIR /srv/

EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]

