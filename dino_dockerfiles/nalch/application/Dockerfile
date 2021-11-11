FROM python:2.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      libpq-dev gettext\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install http://projects.unbit.it/downloads/uwsgi-lts.tar.gz
COPY . .

CMD ["/usr/src/app/entrypoint.sh"]