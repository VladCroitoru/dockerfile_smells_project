FROM python:3
MAINTAINER yigal@publysher.nl

WORKDIR /app/mirigata
EXPOSE 8000

RUN pip install uwsgi

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

RUN adduser --system mirigata
RUN mkdir /app/static && chown mirigata /app/static

# Keep this after pip install, so we have root privs while installing the dependencies
USER mirigata

COPY . /app/

CMD /app/mirigata/docker-entrypoint.sh
