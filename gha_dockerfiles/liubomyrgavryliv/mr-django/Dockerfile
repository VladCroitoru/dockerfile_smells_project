# [START docker]

FROM python:3.8.3-alpine 

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev make libevent-dev build-base

# install dependencies
RUN python -m pip install --upgrade pip

COPY src/requirements/base.txt src/requirements/base.txt
COPY src/requirements/development.txt src/requirements/development.txt
RUN python -m pip install -r src/requirements/development.txt

EXPOSE 8000
WORKDIR /app/src
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# [END docker]