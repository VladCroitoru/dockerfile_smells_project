FROM python:3.7-alpine

WORKDIR /app
COPY requirements.txt requirements.txt

RUN apk update

# openssl is needed for file based sha
RUN apk add openssl libffi-dev libgit2-dev=1.1.0-r2

RUN apk add --no-cache --virtual .build-deps \
  build-base cmake \
  && pip3 install -r requirements.txt \
  && apk del --no-cache .build-deps

COPY source/ source/
COPY tests/ tests/
ADD tests/data/test_source_repo.tar.gz /

ENV PYTHONPATH="/app/source"
ENTRYPOINT [""]
CMD ["python", "/app/source/main.py"]
