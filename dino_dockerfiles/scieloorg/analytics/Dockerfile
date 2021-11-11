FROM python:3.5.2
ENV PYTHONUNBUFFERED 1

MAINTAINER tecnologia@scielo.org

RUN apt-get update && apt-get install -y libmemcached-dev

COPY . /app
COPY production.ini-TEMPLATE /app/config.ini

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install gunicorn && \
    pip install --upgrade deps/scielojcr-1.3.0-py2.py3-none-any.whl && \
    pip install -r requirements.txt && \
    python setup.py install

ENV ANALYTICS_SETTINGS_FILE=/app/config.ini

USER nobody

CMD ["gunicorn", "--paste", "/app/config.ini", "-b", "0.0.0.0", "--forwarded-allow-ips", "*"]
