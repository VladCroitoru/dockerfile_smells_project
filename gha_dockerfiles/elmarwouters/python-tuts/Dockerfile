FROM python:3.8-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip3 install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY woutersmedia_python ./woutersmedia_python

EXPOSE 8000

FROM production as development

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip3 install -r ./requirements/dev.txt

COPY . .