FROM python:3.8-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG uid=1000
ARG gid=1000

RUN addgroup --gid $gid appgroup \
    && adduser --uid $uid --disabled-password --gecos "" --ingroup appgroup appuser

WORKDIR /code

COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev python3-dev tzdata

RUN pip install -r requirements.txt

COPY . .

RUN chown -R appuser:appgroup /code

USER appuser

# ENTRYPOINT python manage.py collectstatic --no-input && python manage.py runserver 0.0.0.0:$PORT

CMD python manage.py collectstatic --no-input && uvicorn --host 0.0.0.0 --port $PORT slack.asgi:application