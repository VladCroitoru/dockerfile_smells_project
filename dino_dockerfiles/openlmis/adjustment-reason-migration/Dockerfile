FROM python:2.7-alpine

COPY requirements.txt /
COPY reason_migration.py /
COPY reason_utils.py /
COPY db.py /
COPY jdbcurl.py /

RUN apk update
RUN apk add postgresql-dev python3-dev musl-dev gcc

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "/reason_migration.py"]
