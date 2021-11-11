FROM python:2-slim

MAINTAINER Gary Reynolds <gary@touch.asn.au>

RUN apt-get update && apt-get -y install libmagic1 libzbar0 && apt-get clean

RUN pip install --no-cache-dir gunicorn pillow python-magic

ARG PIP_EXTRA_ARGS

RUN pip install --no-cache-dir $PIP_EXTRA_ARGS zbar

COPY wsgi.py /

EXPOSE 8000

CMD ["gunicorn", "wsgi", "-b", "0.0.0.0:8000"]
