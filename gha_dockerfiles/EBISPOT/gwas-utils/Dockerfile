FROM python:3.7-slim-buster

COPY . .

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc git openssh-client python-dev libmagic-dev rsync\
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \
    && pip install git+https://github.com/EBISPOT/sum-stats-formatter.git#subdirectory=curator-formatter \
    && apt-get purge -y --auto-remove gcc python-dev git
