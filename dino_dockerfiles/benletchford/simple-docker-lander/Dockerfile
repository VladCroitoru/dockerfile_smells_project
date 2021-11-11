FROM python:3.6

WORKDIR /usr/src/app

COPY simple-docker-lander.py simple-docker-lander.py
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv
RUN pipenv install

ENV PIPENV_DONT_LOAD_ENV=1
ENV PYTHONUNBUFFERED=1

ENTRYPOINT pipenv run python simple-docker-lander.py
