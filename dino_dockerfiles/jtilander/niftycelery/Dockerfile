FROM python:2.7-slim

RUN groupadd user && useradd --create-home --home-dir /app -g user user
WORKDIR /app

RUN pip install redis

ENV CELERY_VERSION 3.1.25

RUN pip install celery=="$CELERY_VERSION"

RUN { \
	echo 'import os'; \
	echo "BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis')"; \
} > celeryconfig.py

ENV CELERY_BROKER_URL redis://redis

USER user
CMD ["celery", "worker"]